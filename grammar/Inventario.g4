// DSL de movimientos de inventario V1.0.
// Los tokens ERROR_* son auxiliares de diagnóstico y no son aceptados por el parser.

grammar Inventario;

// ---------------------------------------------------------------------
// REGLAS DEL PARSER
// ---------------------------------------------------------------------

documento
    : lote EOF
    ;

lote
    : LOTE LLAVE_ABRE listaMovimientos LLAVE_CIERRA
    ;

listaMovimientos
    : movimiento+
    ;

movimiento
    : entrada
    | salida
    | traslado
    | ajuste
    ;

entrada
    : ENTRADA LLAVE_ABRE
      campoSku
      campoCantidad
      campoUbicacionDestino
      campoReferencia
      campoObservacion?
      LLAVE_CIERRA
    ;

salida
    : SALIDA LLAVE_ABRE
      campoSku
      campoCantidad
      campoUbicacionOrigen
      campoReferencia
      campoObservacion?
      LLAVE_CIERRA
    ;

traslado
    : TRASLADO LLAVE_ABRE
      campoSku
      campoCantidad
      campoUbicacionOrigen
      campoUbicacionDestino
      campoReferencia
      campoObservacion?
      LLAVE_CIERRA
    ;

ajuste
    : AJUSTE LLAVE_ABRE
      campoSku
      campoCantidad
      campoTipoAjuste
      campoUbicacion
      campoMotivo
      campoReferencia
      campoObservacion?
      LLAVE_CIERRA
    ;

campoSku
    : CAMPO_SKU DOS_PUNTOS CADENA PUNTO_COMA
    ;

campoCantidad
    : CAMPO_CANTIDAD DOS_PUNTOS ENTERO PUNTO_COMA
    ;

campoUbicacionOrigen
    : CAMPO_UBICACION_ORIGEN DOS_PUNTOS CADENA PUNTO_COMA
    ;

campoUbicacionDestino
    : CAMPO_UBICACION_DESTINO DOS_PUNTOS CADENA PUNTO_COMA
    ;

campoUbicacion
    : CAMPO_UBICACION DOS_PUNTOS CADENA PUNTO_COMA
    ;

campoReferencia
    : CAMPO_REFERENCIA DOS_PUNTOS CADENA PUNTO_COMA
    ;

campoTipoAjuste
    : CAMPO_TIPO_AJUSTE DOS_PUNTOS tipoAjuste PUNTO_COMA
    ;

tipoAjuste
    : INCREMENTO
    | DECREMENTO
    | IDENTIFICADOR
    ;

campoMotivo
    : CAMPO_MOTIVO DOS_PUNTOS CADENA PUNTO_COMA
    ;

campoObservacion
    : CAMPO_OBSERVACION DOS_PUNTOS CADENA PUNTO_COMA
    ;

// ---------------------------------------------------------------------
// TOKENS RESERVADOS. Deben preceder a IDENTIFICADOR.
// ---------------------------------------------------------------------

LOTE                    : 'LOTE';
ENTRADA                 : 'ENTRADA';
SALIDA                  : 'SALIDA';
TRASLADO                : 'TRASLADO';
AJUSTE                  : 'AJUSTE';

CAMPO_SKU               : 'SKU';
CAMPO_CANTIDAD          : 'CANTIDAD';
CAMPO_UBICACION_ORIGEN  : 'UBICACION_ORIGEN';
CAMPO_UBICACION_DESTINO : 'UBICACION_DESTINO';
CAMPO_REFERENCIA        : 'REFERENCIA';
CAMPO_TIPO_AJUSTE       : 'TIPO_AJUSTE';
CAMPO_UBICACION         : 'UBICACION';
CAMPO_MOTIVO            : 'MOTIVO';
CAMPO_OBSERVACION       : 'OBSERVACION';

INCREMENTO              : 'INCREMENTO';
DECREMENTO              : 'DECREMENTO';

// Solo tipoAjuste admite IDENTIFICADOR como valor genérico.
IDENTIFICADOR
    : [A-Z] [A-Z0-9]* ('_' [A-Z0-9]+)*
    ;

// ---------------------------------------------------------------------
// TOKENS AUXILIARES DE DIAGNÓSTICO LÉXICO L01-L05.
// No aparecen en ninguna producción válida del parser.
// ---------------------------------------------------------------------

// L05: literal textual vacío.
ERROR_CADENA_VACIA
    : '""'
    ;

// L02: comilla inicial sin comilla final antes de fin de línea o EOF.
ERROR_CADENA_SIN_CIERRE
    : '"' ~["\r\n]* ('\r'? '\n' | EOF)
    ;

// L03: número decimal, no permitido como cantidad.
ERROR_DECIMAL
    : [0-9]+ '.' [0-9]+
    ;

// L04: entero negativo, no permitido como cantidad.
ERROR_ENTERO_NEGATIVO
    : '-' [0-9]+
    ;

// ---------------------------------------------------------------------
// TOKENS DE LITERALES Y DELIMITADORES
// ---------------------------------------------------------------------

CADENA
    : '"' ~["\r\n\t]+ '"'
    ;

ENTERO
    : [0-9]+
    ;

LLAVE_ABRE
    : '{'
    ;

LLAVE_CIERRA
    : '}'
    ;

DOS_PUNTOS
    : ':'
    ;

PUNTO_COMA
    : ';'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

// L01: cualquier carácter no reconocido. Debe ser la última regla.
ERROR_CARACTER
    : .
    ;
