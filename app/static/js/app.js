"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const formulario = document.getElementById("form-analizador");
    const areaCodigo = document.getElementById("codigo_dsl");
    const archivo = document.getElementById("archivo");
    const nombreArchivo = document.getElementById("nombre-archivo");
    const ejemplo = document.getElementById("ejemplo-dsl");
    const botonEjemplo = document.getElementById("cargar-ejemplo");
    const botonLimpiar = document.getElementById("limpiar");

    if (!formulario || !areaCodigo || !archivo || !ejemplo) return;

    botonEjemplo.addEventListener("click", () => {
        areaCodigo.value = ejemplo.value.trim();
        archivo.value = "";
        nombreArchivo.textContent = "Ningún archivo seleccionado";
        areaCodigo.focus();
    });

    archivo.addEventListener("change", () => {
        nombreArchivo.textContent = archivo.files.length
            ? archivo.files[0].name
            : "Ningún archivo seleccionado";
    });

    botonLimpiar.addEventListener("click", () => {
        areaCodigo.value = "";
        archivo.value = "";
        nombreArchivo.textContent = "Ningún archivo seleccionado";
        const resultados = document.getElementById("resultados");
        if (resultados) resultados.remove();
        const mensajes = document.querySelectorAll(".mensaje");
        mensajes.forEach((mensaje) => mensaje.remove());
        areaCodigo.focus();
    });
});
