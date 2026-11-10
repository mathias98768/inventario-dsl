"""Rutas HTTP de la interfaz mínima de Inventario DSL."""

from __future__ import annotations

from pathlib import PurePosixPath

from flask import Blueprint, render_template, request

from app.services.analizador_service import analizar_texto


web = Blueprint("web", __name__)

EJEMPLO_DSL = '''LOTE {
    ENTRADA {
        SKU: "HER-0001";
        CANTIDAD: 2;
        UBICACION_DESTINO: "A-01-03";
        REFERENCIA: "OC-2026-001";
    }
}'''


@web.get("/")
def inicio():
    return render_template(
        "index.html",
        texto_dsl="",
        ejemplo_dsl=EJEMPLO_DSL,
        resultado=None,
        mensaje=None,
        nombre_origen=None,
    )


@web.post("/analizar")
def analizar():
    texto_formulario = request.form.get("codigo_dsl", "")
    archivo = request.files.get("archivo")
    archivo_seleccionado = archivo is not None and bool(archivo.filename)
    mensaje = None
    nombre_origen = "entrada_web.dsl"

    # Prioridad explícita: un archivo seleccionado prevalece sobre el texto.
    if archivo_seleccionado:
        nombre_archivo = archivo.filename.replace("\\", "/").split("/")[-1]
        extension = PurePosixPath(nombre_archivo).suffix.lower()
        if extension not in {".dsl", ".txt"}:
            return render_template(
                "index.html",
                texto_dsl=texto_formulario,
                ejemplo_dsl=EJEMPLO_DSL,
                resultado=None,
                mensaje="Formato no permitido. Seleccione un archivo .dsl o .txt.",
                nombre_origen=nombre_archivo,
            ), 400

        contenido = archivo.read()
        if not contenido:
            return render_template(
                "index.html",
                texto_dsl=texto_formulario,
                ejemplo_dsl=EJEMPLO_DSL,
                resultado=None,
                mensaje="El archivo seleccionado está vacío.",
                nombre_origen=nombre_archivo,
            ), 400

        try:
            texto_dsl = contenido.decode("utf-8")
        except UnicodeDecodeError:
            return render_template(
                "index.html",
                texto_dsl=texto_formulario,
                ejemplo_dsl=EJEMPLO_DSL,
                resultado=None,
                mensaje="No se pudo leer el archivo. Debe estar codificado en UTF-8.",
                nombre_origen=nombre_archivo,
            ), 400

        nombre_origen = nombre_archivo
        if texto_formulario.strip():
            mensaje = (
                f"Se analizó el archivo {nombre_archivo}. "
                "Cuando se selecciona un archivo, este tiene prioridad "
                "sobre el texto del área."
            )
    else:
        texto_dsl = texto_formulario

    if not texto_dsl.strip():
        return render_template(
            "index.html",
            texto_dsl=texto_dsl,
            ejemplo_dsl=EJEMPLO_DSL,
            resultado=None,
            mensaje="La entrada está vacía. Escriba un lote o seleccione un archivo.",
            nombre_origen=nombre_origen,
        ), 400

    resultado = analizar_texto(texto_dsl, nombre_origen)
    return render_template(
        "index.html",
        texto_dsl=texto_dsl,
        ejemplo_dsl=EJEMPLO_DSL,
        resultado=resultado,
        mensaje=mensaje,
        nombre_origen=nombre_origen,
    )
