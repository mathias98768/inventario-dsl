# Generated from ./grammar/Inventario.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .InventarioParser import InventarioParser
else:
    from InventarioParser import InventarioParser

# This class defines a complete generic visitor for a parse tree produced by InventarioParser.

class InventarioVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by InventarioParser#documento.
    def visitDocumento(self, ctx:InventarioParser.DocumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#lote.
    def visitLote(self, ctx:InventarioParser.LoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#listaMovimientos.
    def visitListaMovimientos(self, ctx:InventarioParser.ListaMovimientosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#movimiento.
    def visitMovimiento(self, ctx:InventarioParser.MovimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#entrada.
    def visitEntrada(self, ctx:InventarioParser.EntradaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#salida.
    def visitSalida(self, ctx:InventarioParser.SalidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#traslado.
    def visitTraslado(self, ctx:InventarioParser.TrasladoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#ajuste.
    def visitAjuste(self, ctx:InventarioParser.AjusteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoSku.
    def visitCampoSku(self, ctx:InventarioParser.CampoSkuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoCantidad.
    def visitCampoCantidad(self, ctx:InventarioParser.CampoCantidadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoUbicacionOrigen.
    def visitCampoUbicacionOrigen(self, ctx:InventarioParser.CampoUbicacionOrigenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoUbicacionDestino.
    def visitCampoUbicacionDestino(self, ctx:InventarioParser.CampoUbicacionDestinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoUbicacion.
    def visitCampoUbicacion(self, ctx:InventarioParser.CampoUbicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoReferencia.
    def visitCampoReferencia(self, ctx:InventarioParser.CampoReferenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoTipoAjuste.
    def visitCampoTipoAjuste(self, ctx:InventarioParser.CampoTipoAjusteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#tipoAjuste.
    def visitTipoAjuste(self, ctx:InventarioParser.TipoAjusteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoMotivo.
    def visitCampoMotivo(self, ctx:InventarioParser.CampoMotivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioParser#campoObservacion.
    def visitCampoObservacion(self, ctx:InventarioParser.CampoObservacionContext):
        return self.visitChildren(ctx)



del InventarioParser
