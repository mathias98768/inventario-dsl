# Inventario DSL

Prototipo de un lenguaje específico de dominio (DSL) para representar y validar movimientos de inventario. El proyecto utiliza ANTLR 4.13.2 para el análisis léxico y sintáctico, un visitor para transformar el árbol sintáctico en estructuras Python y un validador semántico para comprobar las reglas de negocio M01-M09.

El prototipo procesa lotes completos en orden secuencial. La validación se realiza sobre una copia temporal del stock: si algún movimiento incumple una regla, se rechaza el lote completo. Cuando el lote es aceptado, se genera un JSON con los movimientos interpretados y el stock proyectado. **El programa no modifica `data/stock.json` ni confirma cambios en un inventario real.**

## Estado del proyecto

- Gramática `grammar/Inventario.g4` generada con ANTLR 4.13.2.
- Lexer, parser y visitor de Python incluidos en `generated/`.
- Runtime de Python fijado en `antlr4-python3-runtime==4.13.2`.
- 31 escenarios de integración/regresión ejecutados localmente: 6 válidos, 5 léxicos, 8 sintácticos y 12 semánticos. En la última ejecución, los 31 devolvieron el código de salida esperado y no se registraron fallos.
- La batería descrita es una colección de casos manuales ejecutados desde PowerShell; no es una suite de `pytest`.
- Se incorpora una interfaz web local mediante Flask. La ejecución por consola se conserva.

## 1. Requisitos

Para ejecutar el programa:

- Python 3.10 o superior.
- `antlr4-python3-runtime==4.13.2`, instalado desde `requirements.txt`.
- Flask 3.1 o superior y menor que 4, instalado desde `requirements.txt` (solo necesario para la interfaz web).

Para volver a generar los módulos de ANTLR también se necesita:

- Java disponible en `PATH`.
- ANTLR 4.13.2 complete JAR.

Los módulos generados se incluyen en el repositorio, por lo que Java y el JAR no son necesarios para una ejecución normal si no se modifica la gramática. La versión del generador y la del runtime deben mantenerse alineadas cuando se regenere el código.

Entorno local en el que se verificó la versión anterior del núcleo: Windows 11, Python 3.14.3, Eclipse Temurin OpenJDK 25.0.1 y ANTLR 4.13.2.

## 2. Instalación en Windows (PowerShell)

Abre PowerShell en la carpeta raíz del repositorio `inventario-dsl/`.

Comprueba Python:

```powershell
py -3 --version
```

Crea y activa un entorno virtual:

```powershell
py -3 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Regeneración opcional de lexer, parser y visitor

Esta sección solo es necesaria si modificas `grammar/Inventario.g4` o deseas regenerar los módulos. Descarga ANTLR 4.13.2 desde el sitio oficial y guarda el archivo `antlr-4.13.2-complete.jar` en la raíz del proyecto:

<https://www.antlr.org/download/antlr-4.13.2-complete.jar>

También puedes descargarlo desde PowerShell:

```powershell
Invoke-WebRequest -Uri "https://www.antlr.org/download/antlr-4.13.2-complete.jar" -OutFile ".\antlr-4.13.2-complete.jar"
```

Desde la raíz del repositorio, ejecuta:

```powershell
java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o .\generated .\grammar\Inventario.g4
```

La generación produce, entre otros, estos módulos:

- `generated/InventarioLexer.py`
- `generated/InventarioParser.py`
- `generated/InventarioVisitor.py`

Los archivos auxiliares `.tokens` e `.interp` también se conservan en `generated/`.

## 4. Ejecución

Desde la raíz del repositorio, con el entorno virtual activado:

```powershell
python -m src.main .\casos\validos\valido_entrada.dsl
```

Para indicar explícitamente las carpetas de datos y salida:

```powershell
python -m src.main .\casos\validos\valido_entrada.dsl --datos .\data --salida-dir .\salidas
```

Cuando un lote supera las tres fases, el programa genera un archivo JSON en `salidas/`. Si el lote es rechazado, no genera un JSON de aceptación.

Códigos de salida utilizados por el programa:

- `0`: lote aceptado.
- `1`: lote rechazado por errores léxicos, sintácticos o semánticos.

## 5. Flujo de procesamiento

1. Se lee el archivo DSL.
2. El lexer identifica los tokens y permite detectar los errores léxicos L01-L05. Si hay errores léxicos, el procesamiento se detiene.
3. Si el análisis léxico es correcto, el parser evalúa la estructura a partir de la regla inicial `documento`.
4. El listener informa los errores sintácticos y los clasifica en S01-S08.
5. Si la estructura es válida, `VisitorMovimientos` transforma el árbol sintáctico en movimientos representados mediante estructuras Python.
6. `ValidadorSemantico` carga los datos maestros JSON y evalúa M01-M09 siguiendo el orden de los movimientos del lote.
7. El stock se proyecta sobre una copia temporal. Si un movimiento produce un error, el lote completo se rechaza.
8. Si todo el lote es válido, se genera un JSON con los movimientos y el stock proyectado. `data/stock.json` permanece sin modificaciones.

## 6. Reglas de validación

### Errores léxicos

| Código | Descripción |
|---|---|
| L01 | Carácter no reconocido. |
| L02 | Cadena de texto sin comilla de cierre. |
| L03 | Cantidad decimal; las cantidades se expresan como enteros. |
| L04 | Cantidad negativa. |
| L05 | Cadena de texto vacía. |

### Errores sintácticos

| Código | Descripción |
|---|---|
| S01 | Falta el separador `:` entre el campo y su valor. |
| S02 | Falta el terminador `;` del campo. |
| S03 | Falta una llave de cierre. |
| S04 | Falta un campo obligatorio. |
| S05 | Los campos aparecen fuera del orden establecido. |
| S06 | Campo duplicado dentro del movimiento. |
| S07 | Campo que no pertenece a la estructura del movimiento. |
| S08 | El lote no contiene movimientos. |

### Reglas semánticas

| Código | Descripción |
|---|---|
| M01 | El SKU debe existir en el catálogo de productos. |
| M02 | La ubicación debe estar registrada. |
| M03 | La cantidad debe ser mayor que cero. |
| M04 | El stock no puede quedar negativo durante la secuencia del lote. |
| M05 | El origen y el destino de un traslado deben ser diferentes. |
| M06 | La referencia debe existir y ser compatible con el tipo de movimiento. |
| M07 | El tipo de ajuste debe ser `INCREMENTO` o `DECREMENTO`. |
| M08 | El motivo del ajuste debe estar autorizado. |
| M09 | La cantidad del movimiento no debe superar la cantidad documentada. |

## 7. Datos de ejemplo

Los archivos de `data/` contienen datos ficticios destinados a ejecutar el prototipo:

- `productos.json`: catálogo de productos y SKU.
- `ubicaciones.json`: ubicaciones registradas.
- `referencias.json`: referencias documentales, tipos compatibles y cantidades documentadas.
- `motivos.json`: motivos de ajuste autorizados.
- `stock.json`: saldos iniciales por producto y ubicación.

Estos datos no representan información de una empresa real.

## 8. Casos de prueba

Los archivos `.dsl` de `casos/` cubren los siguientes grupos:

| Carpeta | Cantidad | Objetivo |
|---|---:|---|
| `casos/validos/` | 6 | Aceptar entradas, salidas, traslados, ajustes y un lote combinado. |
| `casos/lexicos/` | 5 | Detectar L01-L05. |
| `casos/sintacticos/` | 8 | Detectar S01-S08. |
| `casos/semanticos/` | 12 | Detectar M01-M09 y comprobar rechazo integral y saldo acumulado. |
| **Total** | **31** | **Casos ejecutados en la regresión local descrita durante el desarrollo.** |

### Ejecutar una prueba individual

```powershell
python -m src.main .\casos\validos\valido_completo.dsl
python -m src.main .\casos\lexicos\error_l01.dsl
python -m src.main .\casos\sintacticos\error_s01.dsl
python -m src.main .\casos\semanticos\error_m01.dsl
```

### Ejecutar la regresión completa y comparar códigos de salida

El siguiente bloque ejecuta los 31 archivos y compara el código de salida real con el esperado. Se considera correcto que un archivo válido termine con `0` y que uno diseñado para ser rechazado termine con `1`.

```powershell
$pruebas = @()

Get-ChildItem .\casos\validos\*.dsl | ForEach-Object {
    $pruebas += [PSCustomObject]@{ Archivo = $_; Esperado = 0 }
}

Get-ChildItem .\casos\lexicos\*.dsl | ForEach-Object {
    $pruebas += [PSCustomObject]@{ Archivo = $_; Esperado = 1 }
}

Get-ChildItem .\casos\sintacticos\*.dsl | ForEach-Object {
    $pruebas += [PSCustomObject]@{ Archivo = $_; Esperado = 1 }
}

Get-ChildItem .\casos\semanticos\*.dsl | ForEach-Object {
    $esperado = if ($_.Name -eq "saldo_acumulado_valido.dsl") { 0 } else { 1 }
    $pruebas += [PSCustomObject]@{ Archivo = $_; Esperado = $esperado }
}

$correctas = 0
$total = $pruebas.Count

foreach ($prueba in $pruebas) {
    python -m src.main $prueba.Archivo.FullName *> $null
    $obtenido = $LASTEXITCODE

    if ($obtenido -eq $prueba.Esperado) {
        Write-Host "[OK] $($prueba.Archivo.Name)"
        $correctas++
    }
    else {
        Write-Host "[ERROR] $($prueba.Archivo.Name) - Esperado: $($prueba.Esperado), obtenido: $obtenido"
    }
}

Write-Host "`n========== RESUMEN =========="
Write-Host "Pruebas ejecutadas: $total"
Write-Host "Pruebas correctas: $correctas"
Write-Host "Pruebas fallidas: $($total - $correctas)"
```

En la ejecución de regresión realizada durante el desarrollo se obtuvieron 31 pruebas correctas y 0 fallidas. El bloque anterior permite repetir la comprobación en otro entorno.

## 9. Estructura del repositorio

```text
inventario-dsl/
├── README.md
├── requirements.txt
├── .gitignore
├── run.py
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── analizador_service.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── app.js
├── grammar/
│   └── Inventario.g4
├── generated/
│   ├── InventarioLexer.py
│   ├── InventarioParser.py
│   ├── InventarioVisitor.py
│   ├── Inventario.interp
│   ├── Inventario.tokens
│   ├── InventarioLexer.interp
│   ├── InventarioLexer.tokens
│   └── __init__.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── visitor_movimientos.py
│   └── validador_semantico.py
├── data/
│   ├── productos.json
│   ├── ubicaciones.json
│   ├── referencias.json
│   ├── motivos.json
│   └── stock.json
├── casos/
│   ├── validos/
│   ├── lexicos/
│   ├── sintacticos/
│   └── semanticos/
├── docs/
│   └── evidencias/
└── salidas/
```

- `grammar/`: gramática fuente del lenguaje.
- `generated/`: lexer, parser y visitor generados por ANTLR 4.13.2, junto con sus archivos auxiliares.
- `src/`: punto de entrada por consola, visitor y validador semántico.
- `app/`: rutas, servicio de análisis, plantilla HTML, CSS y JavaScript de la interfaz web.
- `data/`: catálogos y stock inicial de ejemplo.
- `casos/`: archivos DSL para las pruebas.
- `docs/evidencias/`: espacio reservado para evidencias del desarrollo y ejecución.
- `salidas/`: contiene únicamente `.gitkeep` en el repositorio; los JSON generados localmente se excluyen mediante `.gitignore`.

## 10. Límites del prototipo

- La interfaz web Flask es local y sirve para ingresar, cargar y analizar lotes; no implementa autenticación ni administración de usuarios.
- No persiste movimientos en una base de datos.
- No actualiza el stock definitivo ni se conecta con un sistema empresarial.
- Los datos maestros son ficticios y sirven para demostrar el análisis y la validación.
- La validación semántica produce un stock proyectado; no equivale a confirmar una transacción real.

## 11. Ejecución de la interfaz web Flask

La interfaz web es una integración del analizador existente. No reemplaza el núcleo ANTLR ni elimina la ejecución por consola. Ambas modalidades están disponibles:

- Consola: `python -m src.main .\casos\validos\valido_entrada.dsl`
- Web: `python run.py`

### Iniciar Flask

Desde la raíz del repositorio, con el entorno virtual activado y las dependencias instaladas:

```powershell
python run.py
```

Abre en el navegador:

```text
http://127.0.0.1:5000
```

El servidor incluido es el servidor local de desarrollo de Flask.

### Analizar texto escrito

Escribe un lote en el área de texto y presiona **Analizar**. También puedes presionar **Cargar ejemplo** para insertar una ENTRADA compatible con los datos de ejemplo incluidos en `data/`.

### Cargar un archivo

Selecciona un archivo con extensión `.dsl` o `.txt` y presiona **Analizar**. La lectura se realiza en memoria mediante UTF-8; el archivo no se almacena permanentemente. Si se selecciona un archivo y también hay texto en el área, **el archivo tiene prioridad**. El contenido analizado vuelve a mostrarse en el área de texto.

### Resultados mostrados

La interfaz presenta el estado general, la fase alcanzada, los tokens y lexemas con sus posiciones, los errores detectados, el árbol sintáctico, los movimientos extraídos por el visitor y el JSON cuando el lote es aceptado.

La integración web utiliza el mismo visitor y validador semántico del programa de consola. La validación web se realiza en memoria: **no modifica `data/stock.json` ni escribe el JSON de aceptación en `salidas/`**. El JSON se muestra directamente en la página.

### Mantener la ejecución por consola

La incorporación de Flask no reemplaza `src/main.py`. El comando original sigue siendo:

```powershell
python -m src.main .\casos\validos\valido_entrada.dsl
```
