"""Adaptador en memoria entre el analizador ANTLR existente y Flask."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from antlr4 import CommonTokenStream, InputStream

from generated.InventarioLexer import InventarioLexer
from generated.InventarioParser import InventarioParser
from src.main import LEXICAL_ERRORS, ListenerSintactico
from src.validador_semantico import (
    ErrorDatosMaestros,
    ValidadorSemantico,
    stock_a_lista,
)
from src.visitor_movimientos import VisitorMovimientos


DIRECTORIO_PROYECTO = Path(__file__).resolve().parents[2]
DIRECTORIO_DATOS = DIRECTORIO_PROYECTO / "data"


def _resultado_base() -> dict[str, Any]:
    """Construye la respuesta con el formato común de todas las fases."""
    return {
        "aceptado": False,
        "fase": "entrada",
        "tokens": [],
        "errores": [],
        "arbol": None,
        "movimientos": [],
        "resultado_json": None,
        "stock_modificado": False,
    }


def _nombre_token(lexer: InventarioLexer, tipo: int) -> str:
    """Obtiene el nombre simbólico del token generado por ANTLR."""
    nombres = lexer.symbolicNames
    if 0 <= tipo < len(nombres):
        nombre = nombres[tipo]
        if nombre and nombre != "<INVALID>":
            return nombre
    return str(tipo)


def _serializar_tokens(lexer: InventarioLexer, tokens: list[Any]) -> list[dict[str, Any]]:
    """Convierte los tokens de ANTLR en filas aptas para presentar en HTML."""
    return [
        {
            "nombre": _nombre_token(lexer, token.type),
            "lexema": token.text or "",
            "linea": token.line,
            "columna": token.column + 1,
        }
        for token in tokens
    ]


def _error(
    fase: str,
    codigo: str,
    linea: int,
    columna: int,
    lexema: str,
    descripcion: str,
) -> dict[str, Any]:
    return {
        "fase": fase,
        "codigo": codigo,
        "linea": linea,
        "columna": columna,
        "lexema": lexema,
        "descripcion": descripcion,
    }


def analizar_texto(
    texto_dsl: str,
    nombre_origen: str = "entrada_web.dsl",
) -> dict[str, Any]:
    """Analiza un texto DSL sin crear archivos ni modificar el stock definitivo.

    Reutiliza el lexer, parser, listener, visitor y validador del proyecto.
    El resultado contiene únicamente valores serializables por JSON.
    """
    resultado = _resultado_base()

    if not isinstance(texto_dsl, str) or not texto_dsl.strip():
        resultado["errores"].append(
            _error(
                "entrada", "ENTRADA_VACIA", 1, 1, "",
                "Debe escribir o cargar un lote DSL antes de analizar.",
            )
        )
        return resultado

    # Primera pasada: obtener todos los tokens y detectar L01-L05.
    lexer = InventarioLexer(InputStream(texto_dsl))
    lexer.removeErrorListeners()
    tokens_lexicos = lexer.getAllTokens()
    resultado["tokens"] = _serializar_tokens(lexer, tokens_lexicos)

    errores_lexicos = []
    for token in tokens_lexicos:
        diagnostico = LEXICAL_ERRORS.get(token.type)
        if diagnostico is None:
            continue
        codigo, descripcion = diagnostico
        errores_lexicos.append(
            _error(
                "lexica",
                codigo,
                token.line,
                token.column + 1,
                token.text or "",
                descripcion,
            )
        )

    if errores_lexicos:
        resultado["fase"] = "lexica"
        resultado["errores"] = errores_lexicos
        return resultado

    # Segunda pasada: crear el flujo desde el inicio para el parser.
    lexer_parser = InventarioLexer(InputStream(texto_dsl))
    lexer_parser.removeErrorListeners()
    flujo_tokens = CommonTokenStream(lexer_parser)
    flujo_tokens.fill()

    parser = InventarioParser(flujo_tokens)
    listener = ListenerSintactico(flujo_tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(listener)

    arbol = parser.documento()
    if listener.errores or parser.getNumberOfSyntaxErrors() > 0:
        resultado["fase"] = "sintactica"
        resultado["errores"] = [
            _error(
                "sintactica",
                error.codigo,
                error.linea,
                error.columna,
                error.lexema,
                error.descripcion,
            )
            for error in listener.errores
        ]
        # El listener actual clasifica el primer error. Este respaldo evita
        # devolver una lista vacía si ANTLR reporta un error sin notificarlo
        # al listener personalizado por alguna condición excepcional.
        if not resultado["errores"]:
            resultado["errores"].append(
                _error(
                    "sintactica", "S05", 1, 1, "",
                    "La estructura del lote no cumple la gramática.",
                )
            )
        return resultado

    resultado["arbol"] = arbol.toStringTree(recog=parser)

    movimientos_objeto = VisitorMovimientos().visit(arbol)
    resultado["movimientos"] = [
        movimiento.a_dict() for movimiento in movimientos_objeto
    ]

    try:
        validador = ValidadorSemantico(DIRECTORIO_DATOS)
        resultado_semantico = validador.validar(movimientos_objeto)
    except ErrorDatosMaestros as exc:
        resultado["fase"] = "semantica"
        resultado["errores"] = [
            _error(
                "semantica", "DATOS_MAESTROS", 1, 1, "", str(exc)
            )
        ]
        return resultado

    if resultado_semantico.errores:
        resultado["fase"] = "semantica"
        resultado["errores"] = [
            _error(
                "semantica",
                error.codigo,
                error.linea,
                error.columna,
                error.lexema,
                error.descripcion,
            )
            for error in resultado_semantico.errores
        ]
        return resultado

    resultado["aceptado"] = True
    resultado["fase"] = "completa"
    resultado["resultado_json"] = {
        "estado": "ACEPTADO",
        "archivo_origen": Path(nombre_origen).name,
        "movimientos": resultado["movimientos"],
        "stock_proyectado": stock_a_lista(
            resultado_semantico.stock_proyectado
        ),
        "nota": (
            "El stock_proyectado es temporal; la validación no modifica "
            "data/stock.json."
        ),
    }
    # El servicio web solo valida. Nunca persiste la proyección.
    resultado["stock_modificado"] = False
    return resultado
