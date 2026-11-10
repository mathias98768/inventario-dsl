"""Validación semántica transaccional M01-M09 para lotes de inventario."""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.visitor_movimientos import MovimientoInventario


@dataclass(frozen=True)
class ErrorSemantico:
    codigo: str
    linea: int
    columna: int
    lexema: str
    descripcion: str


@dataclass
class ResultadoSemantico:
    errores: list[ErrorSemantico]
    stock_proyectado: dict[tuple[str, str], int]

    @property
    def aceptado(self) -> bool:
        return not self.errores


class ErrorDatosMaestros(Exception):
    """Indica que los JSON de datos maestros no tienen el formato esperado."""


def _leer_json(ruta: Path) -> dict[str, Any]:
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
    except (OSError, json.JSONDecodeError) as exc:
        raise ErrorDatosMaestros(f"No se pudo cargar {ruta.name}: {exc}") from exc
    if not isinstance(contenido, dict):
        raise ErrorDatosMaestros(f"{ruta.name} debe contener un objeto JSON.")
    return contenido


class ValidadorSemantico:
    """Comprueba M01-M09 usando una copia temporal del stock."""

    TIPOS_MOVIMIENTO = {"ENTRADA", "SALIDA", "TRASLADO", "AJUSTE"}
    TIPOS_AJUSTE = {"INCREMENTO", "DECREMENTO"}

    def __init__(self, directorio_datos: Path) -> None:
        self.directorio_datos = Path(directorio_datos)
        self.productos = self._cargar_productos()
        self.ubicaciones = self._cargar_ubicaciones()
        self.referencias = self._cargar_referencias()
        self.motivos = self._cargar_motivos()
        self.stock_inicial = self._cargar_stock()

    def _cargar_productos(self) -> set[str]:
        data = _leer_json(self.directorio_datos / "productos.json")
        try:
            return {
                item["sku"]
                for item in data["productos"]
                if item.get("activo", True)
            }
        except (KeyError, TypeError) as exc:
            raise ErrorDatosMaestros("Formato inválido en productos.json.") from exc

    def _cargar_ubicaciones(self) -> set[str]:
        data = _leer_json(self.directorio_datos / "ubicaciones.json")
        try:
            return {
                item["codigo"]
                for item in data["ubicaciones"]
                if item.get("activa", True)
            }
        except (KeyError, TypeError) as exc:
            raise ErrorDatosMaestros("Formato inválido en ubicaciones.json.") from exc

    def _cargar_referencias(self) -> dict[str, dict[str, Any]]:
        data = _leer_json(self.directorio_datos / "referencias.json")
        try:
            return {
                item["codigo"]: item
                for item in data["referencias"]
                if item.get("activa", True)
            }
        except (KeyError, TypeError) as exc:
            raise ErrorDatosMaestros("Formato inválido en referencias.json.") from exc

    def _cargar_motivos(self) -> set[str]:
        data = _leer_json(self.directorio_datos / "motivos.json")
        try:
            return set(data["motivos_autorizados"])
        except (KeyError, TypeError) as exc:
            raise ErrorDatosMaestros("Formato inválido en motivos.json.") from exc

    def _cargar_stock(self) -> dict[tuple[str, str], int]:
        data = _leer_json(self.directorio_datos / "stock.json")
        try:
            resultado: dict[tuple[str, str], int] = {}
            for item in data["stock"]:
                clave = (item["sku"], item["ubicacion"])
                cantidad = int(item["cantidad"])
                if cantidad < 0:
                    raise ErrorDatosMaestros("El stock inicial no puede ser negativo.")
                resultado[clave] = cantidad
            return resultado
        except (KeyError, TypeError, ValueError) as exc:
            if isinstance(exc, ErrorDatosMaestros):
                raise
            raise ErrorDatosMaestros("Formato inválido en stock.json.") from exc

    @staticmethod
    def _posicion(movimiento: MovimientoInventario, campo: str) -> tuple[int, int]:
        return movimiento.posiciones.get(campo, (movimiento.linea, movimiento.columna))

    def _error(
        self,
        errores: list[ErrorSemantico],
        movimiento: MovimientoInventario,
        codigo: str,
        campo: str,
        lexema: str,
        descripcion: str,
    ) -> None:
        linea, columna = self._posicion(movimiento, campo)
        errores.append(ErrorSemantico(codigo, linea, columna, lexema, descripcion))

    def validar(
        self, movimientos: list[MovimientoInventario]
    ) -> ResultadoSemantico:
        """Evalúa el lote en orden sin alterar el stock definitivo.

        Cada movimiento que incumple una regla no modifica la copia temporal.
        Si existe al menos un error, el lote completo se rechaza y la copia no
        se confirma en ningún archivo.
        """
        stock_temporal = copy.deepcopy(self.stock_inicial)
        errores: list[ErrorSemantico] = []

        for movimiento in movimientos:
            errores_antes = len(errores)

            # M01: el producto debe existir.
            if movimiento.sku not in self.productos:
                self._error(
                    errores, movimiento, "M01", "sku", movimiento.sku,
                    f"El producto {movimiento.sku} no existe en el catálogo.",
                )

            # M02: todas las ubicaciones declaradas deben existir.
            ubicaciones_usadas: list[tuple[str, str]] = []
            if movimiento.ubicacion_origen is not None:
                ubicaciones_usadas.append(("ubicacion_origen", movimiento.ubicacion_origen))
            if movimiento.ubicacion_destino is not None:
                ubicaciones_usadas.append(("ubicacion_destino", movimiento.ubicacion_destino))
            if movimiento.ubicacion is not None:
                ubicaciones_usadas.append(("ubicacion", movimiento.ubicacion))
            for campo, codigo_ubicacion in ubicaciones_usadas:
                if codigo_ubicacion not in self.ubicaciones:
                    self._error(
                        errores, movimiento, "M02", campo, codigo_ubicacion,
                        f"La ubicación {codigo_ubicacion} no está registrada.",
                    )

            # M03: la cantidad debe ser estrictamente positiva.
            if movimiento.cantidad <= 0:
                self._error(
                    errores, movimiento, "M03", "cantidad", str(movimiento.cantidad),
                    "La cantidad debe ser mayor que cero.",
                )

            # M05: origen y destino de un traslado deben ser distintos.
            if (
                movimiento.tipo == "TRASLADO"
                and movimiento.ubicacion_origen == movimiento.ubicacion_destino
            ):
                self._error(
                    errores, movimiento, "M05", "ubicacion_destino",
                    str(movimiento.ubicacion_destino),
                    "El origen y el destino del traslado deben ser diferentes.",
                )

            # M06: la referencia debe existir y corresponder al movimiento.
            referencia = self.referencias.get(movimiento.referencia)
            if referencia is None:
                self._error(
                    errores, movimiento, "M06", "referencia", movimiento.referencia,
                    f"La referencia {movimiento.referencia} no está registrada.",
                )
            elif referencia.get("tipo_movimiento") != movimiento.tipo:
                self._error(
                    errores, movimiento, "M06", "referencia", movimiento.referencia,
                    f"La referencia {movimiento.referencia} no corresponde a {movimiento.tipo}.",
                )

            # M07: solo se admiten INCREMENTO y DECREMENTO.
            if movimiento.tipo == "AJUSTE" and movimiento.tipo_ajuste not in self.TIPOS_AJUSTE:
                self._error(
                    errores, movimiento, "M07", "tipo_ajuste",
                    str(movimiento.tipo_ajuste),
                    "El tipo de ajuste debe ser INCREMENTO o DECREMENTO.",
                )

            # M08: el motivo debe estar autorizado.
            if movimiento.tipo == "AJUSTE" and movimiento.motivo not in self.motivos:
                self._error(
                    errores, movimiento, "M08", "motivo", str(movimiento.motivo),
                    f"El motivo {movimiento.motivo} no está autorizado.",
                )

            # M09: cantidad respaldada por el documento.
            if referencia is not None and referencia.get("tipo_movimiento") == movimiento.tipo:
                maximo = int(referencia.get("cantidad_maxima", 0))
                if movimiento.cantidad > maximo:
                    self._error(
                        errores, movimiento, "M09", "cantidad", str(movimiento.cantidad),
                        f"La cantidad {movimiento.cantidad} supera las {maximo} unidades documentadas.",
                    )

            # Si el movimiento ya tiene errores propios, no se aplica ni siquiera
            # a la copia temporal: se evitan efectos derivados de datos inválidos.
            if len(errores) > errores_antes:
                continue

            # Actualización exclusivamente sobre la copia temporal.
            self._aplicar_movimiento(stock_temporal, movimiento, errores)

        return ResultadoSemantico(errores, stock_temporal)

    def _aplicar_movimiento(
        self,
        stock: dict[tuple[str, str], int],
        movimiento: MovimientoInventario,
        errores: list[ErrorSemantico],
    ) -> None:
        cantidad = movimiento.cantidad
        sku = movimiento.sku

        if movimiento.tipo == "ENTRADA":
            clave_destino = (sku, str(movimiento.ubicacion_destino))
            stock[clave_destino] = stock.get(clave_destino, 0) + cantidad
            return

        if movimiento.tipo == "SALIDA":
            clave_origen = (sku, str(movimiento.ubicacion_origen))
            disponible = stock.get(clave_origen, 0)
            if disponible < cantidad:
                self._error(
                    errores, movimiento, "M04", "cantidad", str(cantidad),
                    f"Stock insuficiente: hay {disponible} unidades y se solicitan {cantidad}.",
                )
                return
            stock[clave_origen] = disponible - cantidad
            return

        if movimiento.tipo == "TRASLADO":
            clave_origen = (sku, str(movimiento.ubicacion_origen))
            clave_destino = (sku, str(movimiento.ubicacion_destino))
            disponible = stock.get(clave_origen, 0)
            if disponible < cantidad:
                self._error(
                    errores, movimiento, "M04", "cantidad", str(cantidad),
                    f"Stock insuficiente para el traslado: hay {disponible} unidades y se solicitan {cantidad}.",
                )
                return
            stock[clave_origen] = disponible - cantidad
            stock[clave_destino] = stock.get(clave_destino, 0) + cantidad
            return

        if movimiento.tipo == "AJUSTE":
            clave = (sku, str(movimiento.ubicacion))
            disponible = stock.get(clave, 0)
            if movimiento.tipo_ajuste == "INCREMENTO":
                stock[clave] = disponible + cantidad
            elif movimiento.tipo_ajuste == "DECREMENTO":
                if disponible < cantidad:
                    self._error(
                        errores, movimiento, "M04", "cantidad", str(cantidad),
                        f"Stock insuficiente para el decremento: hay {disponible} unidades y se solicitan {cantidad}.",
                    )
                    return
                stock[clave] = disponible - cantidad


def stock_a_lista(stock: dict[tuple[str, str], int]) -> list[dict[str, object]]:
    """Convierte el stock proyectado a una lista ordenada apta para JSON."""
    return [
        {"sku": sku, "ubicacion": ubicacion, "cantidad": cantidad}
        for (sku, ubicacion), cantidad in sorted(stock.items())
    ]
