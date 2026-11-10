"""Punto de entrada de la validación léxica, sintáctica y semántica."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener

from generated.InventarioLexer import InventarioLexer
from generated.InventarioParser import InventarioParser
from src.validador_semantico import (
    ErrorDatosMaestros,
    ValidadorSemantico,
    stock_a_lista,
)
from src.visitor_movimientos import VisitorMovimientos


LEXICAL_ERRORS = {
    InventarioLexer.ERROR_CARACTER: (
        "L01", "Carácter no reconocido por el lenguaje."
    ),
    InventarioLexer.ERROR_CADENA_SIN_CIERRE: (
        "L02", "Cadena de texto sin comilla de cierre."
    ),
    InventarioLexer.ERROR_DECIMAL: (
        "L03", "Las cantidades deben expresarse mediante números enteros."
    ),
    InventarioLexer.ERROR_ENTERO_NEGATIVO: (
        "L04", "Las cantidades no admiten signo negativo."
    ),
    InventarioLexer.ERROR_CADENA_VACIA: (
        "L05", "El valor de texto no puede estar vacío."
    ),
}

FIELD_TOKENS = {
    InventarioLexer.CAMPO_SKU,
    InventarioLexer.CAMPO_CANTIDAD,
    InventarioLexer.CAMPO_UBICACION_ORIGEN,
    InventarioLexer.CAMPO_UBICACION_DESTINO,
    InventarioLexer.CAMPO_REFERENCIA,
    InventarioLexer.CAMPO_TIPO_AJUSTE,
    InventarioLexer.CAMPO_UBICACION,
    InventarioLexer.CAMPO_MOTIVO,
    InventarioLexer.CAMPO_OBSERVACION,
}

MOVEMENT_ORDERS = {
    InventarioLexer.ENTRADA: [
        InventarioLexer.CAMPO_SKU,
        InventarioLexer.CAMPO_CANTIDAD,
        InventarioLexer.CAMPO_UBICACION_DESTINO,
        InventarioLexer.CAMPO_REFERENCIA,
        InventarioLexer.CAMPO_OBSERVACION,
    ],
    InventarioLexer.SALIDA: [
        InventarioLexer.CAMPO_SKU,
        InventarioLexer.CAMPO_CANTIDAD,
        InventarioLexer.CAMPO_UBICACION_ORIGEN,
        InventarioLexer.CAMPO_REFERENCIA,
        InventarioLexer.CAMPO_OBSERVACION,
    ],
    InventarioLexer.TRASLADO: [
        InventarioLexer.CAMPO_SKU,
        InventarioLexer.CAMPO_CANTIDAD,
        InventarioLexer.CAMPO_UBICACION_ORIGEN,
        InventarioLexer.CAMPO_UBICACION_DESTINO,
        InventarioLexer.CAMPO_REFERENCIA,
        InventarioLexer.CAMPO_OBSERVACION,
    ],
    InventarioLexer.AJUSTE: [
        InventarioLexer.CAMPO_SKU,
        InventarioLexer.CAMPO_CANTIDAD,
        InventarioLexer.CAMPO_TIPO_AJUSTE,
        InventarioLexer.CAMPO_UBICACION,
        InventarioLexer.CAMPO_MOTIVO,
        InventarioLexer.CAMPO_REFERENCIA,
        InventarioLexer.CAMPO_OBSERVACION,
    ],
}

MOVEMENT_TOKENS = set(MOVEMENT_ORDERS)


class DiagnosticoSintactico:
    def __init__(self, codigo: str, linea: int, columna: int, lexema: str, descripcion: str):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna
        self.lexema = lexema
        self.descripcion = descripcion


class ListenerSintactico(ErrorListener):
    """Asigna S01-S08 a los patrones estructurales definidos para el DSL."""

    def __init__(self, token_stream: CommonTokenStream) -> None:
        super().__init__()
        self.token_stream = token_stream
        self.errores: list[DiagnosticoSintactico] = []

    def _tokens(self):
        return self.token_stream.tokens

    def _tipo_anterior(self, indice: int) -> Optional[int]:
        tokens = self._tokens()
        if 0 <= indice - 1 < len(tokens):
            return tokens[indice - 1].type
        return None

    def _movimiento_actual(self, indice: int) -> Optional[int]:
        tokens = self._tokens()
        for token in reversed(tokens[:max(indice, 0)]):
            if token.type in MOVEMENT_TOKENS:
                return token.type
            if token.type == InventarioLexer.LLAVE_CIERRA:
                break
        return None

    def _campos_vistos(self, indice: int) -> set[int]:
        vistos: set[int] = set()
        tokens = self._tokens()
        inicio = 0
        for i in range(min(indice - 1, len(tokens) - 1), -1, -1):
            if tokens[i].type in MOVEMENT_TOKENS:
                inicio = i + 1
                break
            if tokens[i].type == InventarioLexer.LLAVE_CIERRA:
                inicio = i + 1
                break
        for token in tokens[inicio:indice]:
            if token.type in FIELD_TOKENS:
                vistos.add(token.type)
        return vistos

    def _tipo_esperado(self, recognizer) -> set[int]:
        try:
            return set(recognizer.getExpectedTokens().toList())
        except (AttributeError, TypeError):
            return set()

    def _faltante_aparece_mas_adelante(self, indice: int, tipo_esperado: int) -> bool:
        """Distingue un campo omitido (S04) de uno desplazado (S05)."""
        tokens = self._tokens()
        movimiento = self._movimiento_actual(indice)
        for token in tokens[indice + 1:]:
            if token.type == InventarioLexer.LLAVE_CIERRA:
                break
            if token.type == movimiento:
                break
            if token.type == tipo_esperado:
                return True
        return False

    def _clasificar(self, recognizer, offending_symbol) -> tuple[str, str]:
        tipo = getattr(offending_symbol, "type", None)
        indice = getattr(offending_symbol, "tokenIndex", -1)
        anterior = self._tipo_anterior(indice)
        tokens = self._tokens()

        # Tokens que pueden representar valores de campos.
        valor_tokens = {
            InventarioLexer.CADENA,
            InventarioLexer.ENTERO,
            InventarioLexer.INCREMENTO,
            InventarioLexer.DECREMENTO,
            InventarioLexer.IDENTIFICADOR,
        }

        # S08: lote vacío.
        if (
            tipo == InventarioLexer.LLAVE_CIERRA
            and anterior == InventarioLexer.LLAVE_ABRE
            and indice >= 2
            and tokens[indice - 2].type == InventarioLexer.LOTE
        ):
            return "S08", "El lote debe contener al menos un movimiento."

        # S01: falta el separador ':' después del campo.
        if anterior in FIELD_TOKENS and tipo in valor_tokens:
            return "S01", "Falta el separador ':' entre el campo y su valor."

        # S02: falta el terminador ';' después del valor.
        if anterior in valor_tokens and tipo in FIELD_TOKENS:
            return "S02", "Falta el terminador ';' del campo."

        # S03: falta una o más llaves de cierre.
        es_fin_archivo = (
            tipo == -1
            or getattr(offending_symbol, "text", None) == "<EOF>"
        )

        if es_fin_archivo:
            balance_llaves = 0

            for token in tokens:
                if token.type == InventarioLexer.LLAVE_ABRE:
                    balance_llaves += 1
                elif token.type == InventarioLexer.LLAVE_CIERRA:
                    balance_llaves -= 1

            if balance_llaves > 0:
                return "S03", "El bloque no tiene la llave de cierre requerida."

        # S07: identificador utilizado como un campo desconocido.
        if (
            tipo == InventarioLexer.IDENTIFICADOR
            and anterior in {
                InventarioLexer.LLAVE_ABRE,
                InventarioLexer.PUNTO_COMA,
            }
        ):
            return "S07", "El campo no pertenece a la estructura del movimiento."

        # Errores relacionados con la secuencia de campos.
        if tipo in FIELD_TOKENS:
            campos_vistos = self._campos_vistos(indice)

            # S06: campo duplicado.
            if tipo in campos_vistos:
                return "S06", "El campo está duplicado dentro del movimiento."

            movimiento = self._movimiento_actual(indice)
            orden = MOVEMENT_ORDERS.get(movimiento, [])

            # OBSERVACION es opcional; los demás campos son obligatorios.
            campos_requeridos = [
                campo for campo in orden
                if campo != InventarioLexer.CAMPO_OBSERVACION
            ]

            pendientes = [
                campo for campo in campos_requeridos
                if campo not in campos_vistos
            ]

            if pendientes:
                campo_esperado = pendientes[0]

                if (
                    tipo in orden
                    and orden.index(tipo) > orden.index(campo_esperado)
                ):
                    # Si el campo esperado aparece después, hay desorden.
                    for token in tokens[indice + 1:]:
                        if token.type == InventarioLexer.LLAVE_CIERRA:
                            break

                        if token.type == campo_esperado:
                            return (
                                "S05",
                                "El campo aparece fuera del orden establecido."
                            )

                    # Si no aparece después, falta un campo obligatorio.
                    return (
                        "S04",
                        "Falta un campo obligatorio del movimiento."
                    )

            return (
                "S05",
                "La secuencia de campos no respeta la estructura del movimiento."
            )

        # S04: se cierra el bloque sin completar todos los campos obligatorios.
        if tipo == InventarioLexer.LLAVE_CIERRA:
            movimiento = self._movimiento_actual(indice)
            orden = MOVEMENT_ORDERS.get(movimiento, [])
            campos_vistos = self._campos_vistos(indice)

            faltantes = [
                campo for campo in orden
                if campo != InventarioLexer.CAMPO_OBSERVACION
                and campo not in campos_vistos
            ]

            if faltantes:
                return (
                    "S04",
                    "Falta un campo obligatorio del movimiento."
                )

        return (
            "S05",
            "La secuencia de campos no respeta la estructura del movimiento."
        )

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e) -> None:
        # Conserva únicamente el primer diagnóstico de cada archivo.
        if self.errores:
            return

        codigo, descripcion = self._clasificar(
            recognizer,
            offendingSymbol
        )

        lexema = getattr(offendingSymbol, "text", None) or "<EOF>"

        self.errores.append(
            DiagnosticoSintactico(
                codigo,
                line,
                column + 1,
                lexema,
                descripcion
            )
        )


def imprimir_diagnostico(fase: str, codigo: str, linea: int, columna: int,
                         lexema: str, descripcion: str) -> None:
    print(
        f"{fase} | {codigo} | línea {linea} | columna {columna} "
        f"| lexema {json.dumps(lexema, ensure_ascii=False)} | {descripcion}"
    )


def argumentos() -> argparse.Namespace:
    base = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Valida archivos DSL de movimientos de inventario."
    )
    parser.add_argument("archivo", help="Ruta del archivo .dsl que se analizará.")
    parser.add_argument(
        "--datos", type=Path, default=base / "data",
        help="Carpeta de datos maestros JSON (por defecto: data).",
    )
    parser.add_argument(
        "--salida-dir", type=Path, default=base / "salidas",
        help="Carpeta para JSON de lotes aceptados (por defecto: salidas).",
    )
    return parser.parse_args()


def ejecutar(ruta_archivo: Path, directorio_datos: Path, directorio_salida: Path) -> int:
    ruta_archivo = Path(ruta_archivo)
    if not ruta_archivo.is_file():
        print(f"ERROR | No existe el archivo: {ruta_archivo}", file=sys.stderr)
        return 2

    try:
        # Primera pasada: cargar todos los tokens y buscar diagnósticos léxicos.
        flujo = FileStream(str(ruta_archivo), encoding="utf-8")
        lexer = InventarioLexer(flujo)
        lexer.removeErrorListeners()
        tokens = lexer.getAllTokens()

        errores_lexicos = 0
        for token in tokens:
            diagnostico = LEXICAL_ERRORS.get(token.type)
            if diagnostico is None:
                continue
            codigo, descripcion = diagnostico
            imprimir_diagnostico(
                "LÉXICO", codigo, token.line, token.column + 1,
                token.text or "", descripcion,
            )
            errores_lexicos += 1

        if errores_lexicos:
            print(f"\nLOTE RECHAZADO: {errores_lexicos} error(es) léxico(s).")
            print("No se ejecutó el parser ni la validación semántica.")
            return 1

        # getAllTokens() consume el lexer. Se crea una segunda instancia para
        # construir CommonTokenStream desde el inicio del archivo.
        lexer = InventarioLexer(FileStream(str(ruta_archivo), encoding="utf-8"))
        lexer.removeErrorListeners()
        flujo_tokens = CommonTokenStream(lexer)
        flujo_tokens.fill()

        parser = InventarioParser(flujo_tokens)
        listener = ListenerSintactico(flujo_tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)

        arbol = parser.documento()
        if listener.errores or parser.getNumberOfSyntaxErrors() > 0:
            for error in listener.errores:
                imprimir_diagnostico(
                    "SINTÁCTICO", error.codigo, error.linea, error.columna,
                    error.lexema, error.descripcion,
                )
            print("\nLOTE RECHAZADO: la estructura no cumple la gramática.")
            print("No se ejecutó la validación semántica.")
            return 1

        print("Análisis léxico y sintáctico: CORRECTO.")
        print("\nÁrbol sintáctico:")
        print(arbol.toStringTree(recog=parser))

        movimientos = VisitorMovimientos().visit(arbol)
        validador = ValidadorSemantico(directorio_datos)
        resultado = validador.validar(movimientos)

        if resultado.errores:
            for error in resultado.errores:
                imprimir_diagnostico(
                    "SEMÁNTICO", error.codigo, error.linea, error.columna,
                    error.lexema, error.descripcion,
                )
            print("\nLOTE RECHAZADO: al menos un movimiento incumple reglas semánticas.")
            print("El stock definitivo no fue modificado.")
            print("No se generó JSON de aceptación.")
            return 1

        directorio_salida.mkdir(parents=True, exist_ok=True)
        ruta_json = directorio_salida / f"{ruta_archivo.stem}_validado.json"
        contenido = {
            "estado": "ACEPTADO",
            "archivo_origen": ruta_archivo.name,
            "movimientos": [movimiento.a_dict() for movimiento in movimientos],
            "stock_proyectado": stock_a_lista(resultado.stock_proyectado),
            "nota": "El stock_proyectado es temporal; la validación no modifica data/stock.json.",
        }
        with ruta_json.open("w", encoding="utf-8") as archivo:
            json.dump(contenido, archivo, ensure_ascii=False, indent=4)
            archivo.write("\n")

        print("\nAnálisis semántico: CORRECTO.")
        print(f"LOTE ACEPTADO. JSON generado: {ruta_json}")
        print("El archivo data/stock.json permanece sin modificaciones.")
        return 0

    except ErrorDatosMaestros as exc:
        print(f"DATOS | CONFIGURACIÓN | {exc}", file=sys.stderr)
        return 2
    except (OSError, UnicodeError) as exc:
        print(f"ARCHIVO | No se pudo leer o escribir: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(
            f"ERROR INTERNO | {type(exc).__name__}: {exc}", file=sys.stderr
        )
        return 2


def main() -> int:
    args = argumentos()
    return ejecutar(args.archivo, args.datos, args.salida_dir)


if __name__ == "__main__":
    raise SystemExit(main())
