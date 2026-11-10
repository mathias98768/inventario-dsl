LOTE {
    ENTRADA {
        SKU: "HER-0001";
        CANTIDAD: 5;
        UBICACION_DESTINO: "A-01-03";
        REFERENCIA: "OC-2026-001";
    }

    SALIDA {
        SKU: "HER-0001";
        CANTIDAD: 3;
        UBICACION_ORIGEN: "A-01-03";
        REFERENCIA: "SAL-2026-002";
    }

    TRASLADO {
        SKU: "HER-0001";
        CANTIDAD: 4;
        UBICACION_ORIGEN: "A-01-03";
        UBICACION_DESTINO: "A-01-04";
        REFERENCIA: "TR-2026-001";
    }

    AJUSTE {
        SKU: "HER-0001";
        CANTIDAD: 2;
        TIPO_AJUSTE: DECREMENTO;
        UBICACION: "A-01-03";
        MOTIVO: "Merma";
        REFERENCIA: "AJ-2026-002";
    }
}
