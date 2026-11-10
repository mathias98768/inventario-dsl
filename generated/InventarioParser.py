# Generated from ./grammar/Inventario.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,150,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,2,4,2,46,8,2,11,2,12,2,47,1,3,1,3,1,3,1,3,3,3,54,8,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,63,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,74,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,86,
        8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,99,8,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,
        16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,0,1,1,0,15,17,139,0,36,1,0,0,0,2,39,
        1,0,0,0,4,45,1,0,0,0,6,53,1,0,0,0,8,55,1,0,0,0,10,66,1,0,0,0,12,
        77,1,0,0,0,14,89,1,0,0,0,16,102,1,0,0,0,18,107,1,0,0,0,20,112,1,
        0,0,0,22,117,1,0,0,0,24,122,1,0,0,0,26,127,1,0,0,0,28,132,1,0,0,
        0,30,137,1,0,0,0,32,139,1,0,0,0,34,144,1,0,0,0,36,37,3,2,1,0,37,
        38,5,0,0,1,38,1,1,0,0,0,39,40,5,1,0,0,40,41,5,24,0,0,41,42,3,4,2,
        0,42,43,5,25,0,0,43,3,1,0,0,0,44,46,3,6,3,0,45,44,1,0,0,0,46,47,
        1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,5,1,0,0,0,49,54,3,8,4,0,50,
        54,3,10,5,0,51,54,3,12,6,0,52,54,3,14,7,0,53,49,1,0,0,0,53,50,1,
        0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,7,1,0,0,0,55,56,5,2,0,0,56,
        57,5,24,0,0,57,58,3,16,8,0,58,59,3,18,9,0,59,60,3,22,11,0,60,62,
        3,26,13,0,61,63,3,34,17,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,
        0,0,64,65,5,25,0,0,65,9,1,0,0,0,66,67,5,3,0,0,67,68,5,24,0,0,68,
        69,3,16,8,0,69,70,3,18,9,0,70,71,3,20,10,0,71,73,3,26,13,0,72,74,
        3,34,17,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,76,5,25,0,
        0,76,11,1,0,0,0,77,78,5,4,0,0,78,79,5,24,0,0,79,80,3,16,8,0,80,81,
        3,18,9,0,81,82,3,20,10,0,82,83,3,22,11,0,83,85,3,26,13,0,84,86,3,
        34,17,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,5,25,0,0,
        88,13,1,0,0,0,89,90,5,5,0,0,90,91,5,24,0,0,91,92,3,16,8,0,92,93,
        3,18,9,0,93,94,3,28,14,0,94,95,3,24,12,0,95,96,3,32,16,0,96,98,3,
        26,13,0,97,99,3,34,17,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,
        0,100,101,5,25,0,0,101,15,1,0,0,0,102,103,5,6,0,0,103,104,5,26,0,
        0,104,105,5,22,0,0,105,106,5,27,0,0,106,17,1,0,0,0,107,108,5,7,0,
        0,108,109,5,26,0,0,109,110,5,23,0,0,110,111,5,27,0,0,111,19,1,0,
        0,0,112,113,5,8,0,0,113,114,5,26,0,0,114,115,5,22,0,0,115,116,5,
        27,0,0,116,21,1,0,0,0,117,118,5,9,0,0,118,119,5,26,0,0,119,120,5,
        22,0,0,120,121,5,27,0,0,121,23,1,0,0,0,122,123,5,12,0,0,123,124,
        5,26,0,0,124,125,5,22,0,0,125,126,5,27,0,0,126,25,1,0,0,0,127,128,
        5,10,0,0,128,129,5,26,0,0,129,130,5,22,0,0,130,131,5,27,0,0,131,
        27,1,0,0,0,132,133,5,11,0,0,133,134,5,26,0,0,134,135,3,30,15,0,135,
        136,5,27,0,0,136,29,1,0,0,0,137,138,7,0,0,0,138,31,1,0,0,0,139,140,
        5,13,0,0,140,141,5,26,0,0,141,142,5,22,0,0,142,143,5,27,0,0,143,
        33,1,0,0,0,144,145,5,14,0,0,145,146,5,26,0,0,146,147,5,22,0,0,147,
        148,5,27,0,0,148,35,1,0,0,0,6,47,53,62,73,85,98
    ]

class InventarioParser ( Parser ):

    grammarFileName = "Inventario.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'LOTE'", "'ENTRADA'", "'SALIDA'", "'TRASLADO'",
                     "'AJUSTE'", "'SKU'", "'CANTIDAD'", "'UBICACION_ORIGEN'",
                     "'UBICACION_DESTINO'", "'REFERENCIA'", "'TIPO_AJUSTE'",
                     "'UBICACION'", "'MOTIVO'", "'OBSERVACION'", "'INCREMENTO'",
                     "'DECREMENTO'", "<INVALID>", "'\"\"'", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "'{'", "'}'", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "LOTE", "ENTRADA", "SALIDA", "TRASLADO",
                      "AJUSTE", "CAMPO_SKU", "CAMPO_CANTIDAD", "CAMPO_UBICACION_ORIGEN",
                      "CAMPO_UBICACION_DESTINO", "CAMPO_REFERENCIA", "CAMPO_TIPO_AJUSTE",
                      "CAMPO_UBICACION", "CAMPO_MOTIVO", "CAMPO_OBSERVACION",
                      "INCREMENTO", "DECREMENTO", "IDENTIFICADOR", "ERROR_CADENA_VACIA",
                      "ERROR_CADENA_SIN_CIERRE", "ERROR_DECIMAL", "ERROR_ENTERO_NEGATIVO",
                      "CADENA", "ENTERO", "LLAVE_ABRE", "LLAVE_CIERRA",
                      "DOS_PUNTOS", "PUNTO_COMA", "WS", "ERROR_CARACTER" ]

    RULE_documento = 0
    RULE_lote = 1
    RULE_listaMovimientos = 2
    RULE_movimiento = 3
    RULE_entrada = 4
    RULE_salida = 5
    RULE_traslado = 6
    RULE_ajuste = 7
    RULE_campoSku = 8
    RULE_campoCantidad = 9
    RULE_campoUbicacionOrigen = 10
    RULE_campoUbicacionDestino = 11
    RULE_campoUbicacion = 12
    RULE_campoReferencia = 13
    RULE_campoTipoAjuste = 14
    RULE_tipoAjuste = 15
    RULE_campoMotivo = 16
    RULE_campoObservacion = 17

    ruleNames =  [ "documento", "lote", "listaMovimientos", "movimiento",
                   "entrada", "salida", "traslado", "ajuste", "campoSku",
                   "campoCantidad", "campoUbicacionOrigen", "campoUbicacionDestino",
                   "campoUbicacion", "campoReferencia", "campoTipoAjuste",
                   "tipoAjuste", "campoMotivo", "campoObservacion" ]

    EOF = Token.EOF
    LOTE=1
    ENTRADA=2
    SALIDA=3
    TRASLADO=4
    AJUSTE=5
    CAMPO_SKU=6
    CAMPO_CANTIDAD=7
    CAMPO_UBICACION_ORIGEN=8
    CAMPO_UBICACION_DESTINO=9
    CAMPO_REFERENCIA=10
    CAMPO_TIPO_AJUSTE=11
    CAMPO_UBICACION=12
    CAMPO_MOTIVO=13
    CAMPO_OBSERVACION=14
    INCREMENTO=15
    DECREMENTO=16
    IDENTIFICADOR=17
    ERROR_CADENA_VACIA=18
    ERROR_CADENA_SIN_CIERRE=19
    ERROR_DECIMAL=20
    ERROR_ENTERO_NEGATIVO=21
    CADENA=22
    ENTERO=23
    LLAVE_ABRE=24
    LLAVE_CIERRA=25
    DOS_PUNTOS=26
    PUNTO_COMA=27
    WS=28
    ERROR_CARACTER=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lote(self):
            return self.getTypedRuleContext(InventarioParser.LoteContext,0)


        def EOF(self):
            return self.getToken(InventarioParser.EOF, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_documento

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocumento" ):
                return visitor.visitDocumento(self)
            else:
                return visitor.visitChildren(self)




    def documento(self):

        localctx = InventarioParser.DocumentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_documento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.lote()
            self.state = 37
            self.match(InventarioParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOTE(self):
            return self.getToken(InventarioParser.LOTE, 0)

        def LLAVE_ABRE(self):
            return self.getToken(InventarioParser.LLAVE_ABRE, 0)

        def listaMovimientos(self):
            return self.getTypedRuleContext(InventarioParser.ListaMovimientosContext,0)


        def LLAVE_CIERRA(self):
            return self.getToken(InventarioParser.LLAVE_CIERRA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_lote

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLote" ):
                return visitor.visitLote(self)
            else:
                return visitor.visitChildren(self)




    def lote(self):

        localctx = InventarioParser.LoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(InventarioParser.LOTE)
            self.state = 40
            self.match(InventarioParser.LLAVE_ABRE)
            self.state = 41
            self.listaMovimientos()
            self.state = 42
            self.match(InventarioParser.LLAVE_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaMovimientosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def movimiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InventarioParser.MovimientoContext)
            else:
                return self.getTypedRuleContext(InventarioParser.MovimientoContext,i)


        def getRuleIndex(self):
            return InventarioParser.RULE_listaMovimientos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaMovimientos" ):
                return visitor.visitListaMovimientos(self)
            else:
                return visitor.visitChildren(self)




    def listaMovimientos(self):

        localctx = InventarioParser.ListaMovimientosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_listaMovimientos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.movimiento()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MovimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entrada(self):
            return self.getTypedRuleContext(InventarioParser.EntradaContext,0)


        def salida(self):
            return self.getTypedRuleContext(InventarioParser.SalidaContext,0)


        def traslado(self):
            return self.getTypedRuleContext(InventarioParser.TrasladoContext,0)


        def ajuste(self):
            return self.getTypedRuleContext(InventarioParser.AjusteContext,0)


        def getRuleIndex(self):
            return InventarioParser.RULE_movimiento

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMovimiento" ):
                return visitor.visitMovimiento(self)
            else:
                return visitor.visitChildren(self)




    def movimiento(self):

        localctx = InventarioParser.MovimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_movimiento)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.entrada()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.salida()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.traslado()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.ajuste()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTRADA(self):
            return self.getToken(InventarioParser.ENTRADA, 0)

        def LLAVE_ABRE(self):
            return self.getToken(InventarioParser.LLAVE_ABRE, 0)

        def campoSku(self):
            return self.getTypedRuleContext(InventarioParser.CampoSkuContext,0)


        def campoCantidad(self):
            return self.getTypedRuleContext(InventarioParser.CampoCantidadContext,0)


        def campoUbicacionDestino(self):
            return self.getTypedRuleContext(InventarioParser.CampoUbicacionDestinoContext,0)


        def campoReferencia(self):
            return self.getTypedRuleContext(InventarioParser.CampoReferenciaContext,0)


        def LLAVE_CIERRA(self):
            return self.getToken(InventarioParser.LLAVE_CIERRA, 0)

        def campoObservacion(self):
            return self.getTypedRuleContext(InventarioParser.CampoObservacionContext,0)


        def getRuleIndex(self):
            return InventarioParser.RULE_entrada

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrada" ):
                return visitor.visitEntrada(self)
            else:
                return visitor.visitChildren(self)




    def entrada(self):

        localctx = InventarioParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_entrada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(InventarioParser.ENTRADA)
            self.state = 56
            self.match(InventarioParser.LLAVE_ABRE)
            self.state = 57
            self.campoSku()
            self.state = 58
            self.campoCantidad()
            self.state = 59
            self.campoUbicacionDestino()
            self.state = 60
            self.campoReferencia()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 61
                self.campoObservacion()


            self.state = 64
            self.match(InventarioParser.LLAVE_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SalidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SALIDA(self):
            return self.getToken(InventarioParser.SALIDA, 0)

        def LLAVE_ABRE(self):
            return self.getToken(InventarioParser.LLAVE_ABRE, 0)

        def campoSku(self):
            return self.getTypedRuleContext(InventarioParser.CampoSkuContext,0)


        def campoCantidad(self):
            return self.getTypedRuleContext(InventarioParser.CampoCantidadContext,0)


        def campoUbicacionOrigen(self):
            return self.getTypedRuleContext(InventarioParser.CampoUbicacionOrigenContext,0)


        def campoReferencia(self):
            return self.getTypedRuleContext(InventarioParser.CampoReferenciaContext,0)


        def LLAVE_CIERRA(self):
            return self.getToken(InventarioParser.LLAVE_CIERRA, 0)

        def campoObservacion(self):
            return self.getTypedRuleContext(InventarioParser.CampoObservacionContext,0)


        def getRuleIndex(self):
            return InventarioParser.RULE_salida

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSalida" ):
                return visitor.visitSalida(self)
            else:
                return visitor.visitChildren(self)




    def salida(self):

        localctx = InventarioParser.SalidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_salida)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(InventarioParser.SALIDA)
            self.state = 67
            self.match(InventarioParser.LLAVE_ABRE)
            self.state = 68
            self.campoSku()
            self.state = 69
            self.campoCantidad()
            self.state = 70
            self.campoUbicacionOrigen()
            self.state = 71
            self.campoReferencia()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 72
                self.campoObservacion()


            self.state = 75
            self.match(InventarioParser.LLAVE_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrasladoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRASLADO(self):
            return self.getToken(InventarioParser.TRASLADO, 0)

        def LLAVE_ABRE(self):
            return self.getToken(InventarioParser.LLAVE_ABRE, 0)

        def campoSku(self):
            return self.getTypedRuleContext(InventarioParser.CampoSkuContext,0)


        def campoCantidad(self):
            return self.getTypedRuleContext(InventarioParser.CampoCantidadContext,0)


        def campoUbicacionOrigen(self):
            return self.getTypedRuleContext(InventarioParser.CampoUbicacionOrigenContext,0)


        def campoUbicacionDestino(self):
            return self.getTypedRuleContext(InventarioParser.CampoUbicacionDestinoContext,0)


        def campoReferencia(self):
            return self.getTypedRuleContext(InventarioParser.CampoReferenciaContext,0)


        def LLAVE_CIERRA(self):
            return self.getToken(InventarioParser.LLAVE_CIERRA, 0)

        def campoObservacion(self):
            return self.getTypedRuleContext(InventarioParser.CampoObservacionContext,0)


        def getRuleIndex(self):
            return InventarioParser.RULE_traslado

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTraslado" ):
                return visitor.visitTraslado(self)
            else:
                return visitor.visitChildren(self)




    def traslado(self):

        localctx = InventarioParser.TrasladoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_traslado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(InventarioParser.TRASLADO)
            self.state = 78
            self.match(InventarioParser.LLAVE_ABRE)
            self.state = 79
            self.campoSku()
            self.state = 80
            self.campoCantidad()
            self.state = 81
            self.campoUbicacionOrigen()
            self.state = 82
            self.campoUbicacionDestino()
            self.state = 83
            self.campoReferencia()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 84
                self.campoObservacion()


            self.state = 87
            self.match(InventarioParser.LLAVE_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AjusteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AJUSTE(self):
            return self.getToken(InventarioParser.AJUSTE, 0)

        def LLAVE_ABRE(self):
            return self.getToken(InventarioParser.LLAVE_ABRE, 0)

        def campoSku(self):
            return self.getTypedRuleContext(InventarioParser.CampoSkuContext,0)


        def campoCantidad(self):
            return self.getTypedRuleContext(InventarioParser.CampoCantidadContext,0)


        def campoTipoAjuste(self):
            return self.getTypedRuleContext(InventarioParser.CampoTipoAjusteContext,0)


        def campoUbicacion(self):
            return self.getTypedRuleContext(InventarioParser.CampoUbicacionContext,0)


        def campoMotivo(self):
            return self.getTypedRuleContext(InventarioParser.CampoMotivoContext,0)


        def campoReferencia(self):
            return self.getTypedRuleContext(InventarioParser.CampoReferenciaContext,0)


        def LLAVE_CIERRA(self):
            return self.getToken(InventarioParser.LLAVE_CIERRA, 0)

        def campoObservacion(self):
            return self.getTypedRuleContext(InventarioParser.CampoObservacionContext,0)


        def getRuleIndex(self):
            return InventarioParser.RULE_ajuste

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAjuste" ):
                return visitor.visitAjuste(self)
            else:
                return visitor.visitChildren(self)




    def ajuste(self):

        localctx = InventarioParser.AjusteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ajuste)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(InventarioParser.AJUSTE)
            self.state = 90
            self.match(InventarioParser.LLAVE_ABRE)
            self.state = 91
            self.campoSku()
            self.state = 92
            self.campoCantidad()
            self.state = 93
            self.campoTipoAjuste()
            self.state = 94
            self.campoUbicacion()
            self.state = 95
            self.campoMotivo()
            self.state = 96
            self.campoReferencia()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 97
                self.campoObservacion()


            self.state = 100
            self.match(InventarioParser.LLAVE_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoSkuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_SKU(self):
            return self.getToken(InventarioParser.CAMPO_SKU, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def CADENA(self):
            return self.getToken(InventarioParser.CADENA, 0)

        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoSku

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoSku" ):
                return visitor.visitCampoSku(self)
            else:
                return visitor.visitChildren(self)




    def campoSku(self):

        localctx = InventarioParser.CampoSkuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_campoSku)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(InventarioParser.CAMPO_SKU)
            self.state = 103
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 104
            self.match(InventarioParser.CADENA)
            self.state = 105
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoCantidadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_CANTIDAD(self):
            return self.getToken(InventarioParser.CAMPO_CANTIDAD, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def ENTERO(self):
            return self.getToken(InventarioParser.ENTERO, 0)

        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoCantidad

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoCantidad" ):
                return visitor.visitCampoCantidad(self)
            else:
                return visitor.visitChildren(self)




    def campoCantidad(self):

        localctx = InventarioParser.CampoCantidadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_campoCantidad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(InventarioParser.CAMPO_CANTIDAD)
            self.state = 108
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 109
            self.match(InventarioParser.ENTERO)
            self.state = 110
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoUbicacionOrigenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_UBICACION_ORIGEN(self):
            return self.getToken(InventarioParser.CAMPO_UBICACION_ORIGEN, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def CADENA(self):
            return self.getToken(InventarioParser.CADENA, 0)

        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoUbicacionOrigen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoUbicacionOrigen" ):
                return visitor.visitCampoUbicacionOrigen(self)
            else:
                return visitor.visitChildren(self)




    def campoUbicacionOrigen(self):

        localctx = InventarioParser.CampoUbicacionOrigenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_campoUbicacionOrigen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(InventarioParser.CAMPO_UBICACION_ORIGEN)
            self.state = 113
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 114
            self.match(InventarioParser.CADENA)
            self.state = 115
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoUbicacionDestinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_UBICACION_DESTINO(self):
            return self.getToken(InventarioParser.CAMPO_UBICACION_DESTINO, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def CADENA(self):
            return self.getToken(InventarioParser.CADENA, 0)

        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoUbicacionDestino

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoUbicacionDestino" ):
                return visitor.visitCampoUbicacionDestino(self)
            else:
                return visitor.visitChildren(self)




    def campoUbicacionDestino(self):

        localctx = InventarioParser.CampoUbicacionDestinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_campoUbicacionDestino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(InventarioParser.CAMPO_UBICACION_DESTINO)
            self.state = 118
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 119
            self.match(InventarioParser.CADENA)
            self.state = 120
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoUbicacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_UBICACION(self):
            return self.getToken(InventarioParser.CAMPO_UBICACION, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def CADENA(self):
            return self.getToken(InventarioParser.CADENA, 0)

        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoUbicacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoUbicacion" ):
                return visitor.visitCampoUbicacion(self)
            else:
                return visitor.visitChildren(self)




    def campoUbicacion(self):

        localctx = InventarioParser.CampoUbicacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_campoUbicacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(InventarioParser.CAMPO_UBICACION)
            self.state = 123
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 124
            self.match(InventarioParser.CADENA)
            self.state = 125
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoReferenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_REFERENCIA(self):
            return self.getToken(InventarioParser.CAMPO_REFERENCIA, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def CADENA(self):
            return self.getToken(InventarioParser.CADENA, 0)

        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoReferencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoReferencia" ):
                return visitor.visitCampoReferencia(self)
            else:
                return visitor.visitChildren(self)




    def campoReferencia(self):

        localctx = InventarioParser.CampoReferenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_campoReferencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(InventarioParser.CAMPO_REFERENCIA)
            self.state = 128
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 129
            self.match(InventarioParser.CADENA)
            self.state = 130
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoTipoAjusteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_TIPO_AJUSTE(self):
            return self.getToken(InventarioParser.CAMPO_TIPO_AJUSTE, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def tipoAjuste(self):
            return self.getTypedRuleContext(InventarioParser.TipoAjusteContext,0)


        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoTipoAjuste

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoTipoAjuste" ):
                return visitor.visitCampoTipoAjuste(self)
            else:
                return visitor.visitChildren(self)




    def campoTipoAjuste(self):

        localctx = InventarioParser.CampoTipoAjusteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_campoTipoAjuste)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(InventarioParser.CAMPO_TIPO_AJUSTE)
            self.state = 133
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 134
            self.tipoAjuste()
            self.state = 135
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoAjusteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENTO(self):
            return self.getToken(InventarioParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(InventarioParser.DECREMENTO, 0)

        def IDENTIFICADOR(self):
            return self.getToken(InventarioParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_tipoAjuste

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoAjuste" ):
                return visitor.visitTipoAjuste(self)
            else:
                return visitor.visitChildren(self)




    def tipoAjuste(self):

        localctx = InventarioParser.TipoAjusteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_tipoAjuste)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoMotivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_MOTIVO(self):
            return self.getToken(InventarioParser.CAMPO_MOTIVO, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def CADENA(self):
            return self.getToken(InventarioParser.CADENA, 0)

        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoMotivo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoMotivo" ):
                return visitor.visitCampoMotivo(self)
            else:
                return visitor.visitChildren(self)




    def campoMotivo(self):

        localctx = InventarioParser.CampoMotivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_campoMotivo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(InventarioParser.CAMPO_MOTIVO)
            self.state = 140
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 141
            self.match(InventarioParser.CADENA)
            self.state = 142
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoObservacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO_OBSERVACION(self):
            return self.getToken(InventarioParser.CAMPO_OBSERVACION, 0)

        def DOS_PUNTOS(self):
            return self.getToken(InventarioParser.DOS_PUNTOS, 0)

        def CADENA(self):
            return self.getToken(InventarioParser.CADENA, 0)

        def PUNTO_COMA(self):
            return self.getToken(InventarioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return InventarioParser.RULE_campoObservacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampoObservacion" ):
                return visitor.visitCampoObservacion(self)
            else:
                return visitor.visitChildren(self)




    def campoObservacion(self):

        localctx = InventarioParser.CampoObservacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_campoObservacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(InventarioParser.CAMPO_OBSERVACION)
            self.state = 145
            self.match(InventarioParser.DOS_PUNTOS)
            self.state = 146
            self.match(InventarioParser.CADENA)
            self.state = 147
            self.match(InventarioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
