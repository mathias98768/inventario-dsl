"""Transforma el árbol de ANTLR en movimientos de Python."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from generated.InventarioVisitor import InventarioVisitor


@dataclass(frozen=True)
class MovimientoInventario:
    """Representación de un movimiento extraído del árbol sintáctico."""

    tipo: str
    sku: str
    cantidad: int
    referencia: str
    ubicacion_origen: Optional[str] = None
    ubicacion_destino: Optional[str] = None
    ubicacion: Optional[str] = None
    tipo_ajuste: Optional[str] = None
    motivo: Optional[str] = None
    observacion: Optional[str] = None
    linea: int = 1
    columna: int = 1
    posiciones: dict[str, tuple[int, int]] = field(default_factory=dict)

    def a_dict(self) -> dict[str, object]:
        """Devuelve los datos de negocio, sin metadatos de posición."""
        resultado: dict[str, object] = {
            "tipo": self.tipo,
            "sku": self.sku,
            "cantidad": self.cantidad,
        }
        for nombre in (
            "ubicacion_origen",
            "ubicacion_destino",
            "ubicacion",
            "tipo_ajuste",
            "motivo",
        ):
            valor = getattr(self, nombre)
            if valor is not None:
                resultado[nombre] = valor
        resultado["referencia"] = self.referencia
        if self.observacion is not None:
            resultado["observacion"] = self.observacion
        return resultado


class VisitorMovimientos(InventarioVisitor):
    """Recorre el CST generado por ANTLR y crea objetos MovimientoInventario."""

    @staticmethod
    def _texto_cadena(terminal) -> str:
        if terminal is None:
            raise ValueError("Se esperaba un token CADENA en un árbol válido.")
        texto = terminal.getText()
        return texto[1:-1]

    @staticmethod
    def _posicion(contexto) -> tuple[int, int]:
        token = contexto.start
        return token.line, token.column + 1

    @staticmethod
    def _contexto_opcional(contexto, nombre_regla: str):
        """Obtiene un subcontexto si la regla aparece en ese movimiento."""
        accessor = getattr(contexto, nombre_regla, None)
        return accessor() if accessor is not None else None

    def visitDocumento(self, ctx):
        return self.visit(ctx.lote())

    def visitLote(self, ctx):
        return self.visit(ctx.listaMovimientos())

    def visitListaMovimientos(self, ctx):
        return [self.visit(movimiento) for movimiento in ctx.movimiento()]

    def visitMovimiento(self, ctx):
        return self.visit(ctx.getChild(0))

    def _crear_movimiento(
        self,
        ctx,
        tipo: str,
        *,
        origen: Optional[str] = None,
        destino: Optional[str] = None,
        ubicacion: Optional[str] = None,
        tipo_ajuste: Optional[str] = None,
        motivo: Optional[str] = None,
    ) -> MovimientoInventario:
        sku_ctx = ctx.campoSku()
        cantidad_ctx = ctx.campoCantidad()
        referencia_ctx = ctx.campoReferencia()
        observacion_ctx = ctx.campoObservacion()

        posiciones = {
            "sku": self._posicion(sku_ctx),
            "cantidad": self._posicion(cantidad_ctx),
            "referencia": self._posicion(referencia_ctx),
        }
        contexto_origen = self._contexto_opcional(ctx, "campoUbicacionOrigen")
        contexto_destino = self._contexto_opcional(ctx, "campoUbicacionDestino")
        contexto_ubicacion = self._contexto_opcional(ctx, "campoUbicacion")
        contexto_tipo = self._contexto_opcional(ctx, "campoTipoAjuste")
        contexto_motivo = self._contexto_opcional(ctx, "campoMotivo")

        if contexto_origen is not None:
            posiciones["ubicacion_origen"] = self._posicion(contexto_origen)
        if contexto_destino is not None:
            posiciones["ubicacion_destino"] = self._posicion(contexto_destino)
        if contexto_ubicacion is not None:
            posiciones["ubicacion"] = self._posicion(contexto_ubicacion)
        if contexto_tipo is not None:
            posiciones["tipo_ajuste"] = self._posicion(contexto_tipo)
        if contexto_motivo is not None:
            posiciones["motivo"] = self._posicion(contexto_motivo)
        if observacion_ctx is not None:
            posiciones["observacion"] = self._posicion(observacion_ctx)

        return MovimientoInventario(
            tipo=tipo,
            sku=self._texto_cadena(sku_ctx.CADENA()),
            cantidad=int(cantidad_ctx.ENTERO().getText()),
            referencia=self._texto_cadena(referencia_ctx.CADENA()),
            ubicacion_origen=origen,
            ubicacion_destino=destino,
            ubicacion=ubicacion,
            tipo_ajuste=tipo_ajuste,
            motivo=motivo,
            observacion=(
                self._texto_cadena(observacion_ctx.CADENA())
                if observacion_ctx is not None
                else None
            ),
            linea=ctx.start.line,
            columna=ctx.start.column + 1,
            posiciones=posiciones,
        )

    def visitEntrada(self, ctx):
        destino = self._texto_cadena(ctx.campoUbicacionDestino().CADENA())
        return self._crear_movimiento(ctx, "ENTRADA", destino=destino)

    def visitSalida(self, ctx):
        origen = self._texto_cadena(ctx.campoUbicacionOrigen().CADENA())
        return self._crear_movimiento(ctx, "SALIDA", origen=origen)

    def visitTraslado(self, ctx):
        origen = self._texto_cadena(ctx.campoUbicacionOrigen().CADENA())
        destino = self._texto_cadena(ctx.campoUbicacionDestino().CADENA())
        return self._crear_movimiento(
            ctx, "TRASLADO", origen=origen, destino=destino
        )

    def visitAjuste(self, ctx):
        tipo_ajuste = ctx.campoTipoAjuste().tipoAjuste().getText()
        ubicacion = self._texto_cadena(ctx.campoUbicacion().CADENA())
        motivo = self._texto_cadena(ctx.campoMotivo().CADENA())
        return self._crear_movimiento(
            ctx,
            "AJUSTE",
            ubicacion=ubicacion,
            tipo_ajuste=tipo_ajuste,
            motivo=motivo,
        )
