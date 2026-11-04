Hello World!
Este es mi primer cambio en GitHub

# Texto a MP3

Aplicación sencilla en Python que convierte cualquier texto en un archivo de
audio **MP3**. Se abre en su propia ventana, como cualquier programa, y también
se puede usar desde la terminal.

## Instalarla en Windows (con ícono en el escritorio)

1. Instala [Python 3](https://www.python.org/downloads/) (3.8 o más reciente).
   Al instalar, marca la casilla **"Add python.exe to PATH"**.
2. Descarga la carpeta de la aplicación y guárdala donde quieras (por ejemplo,
   en **Documentos**).
3. Abre la carpeta y haz doble clic en `Abrir Texto a MP3 (Windows).bat`.

La primera vez tarda un poco, porque prepara la aplicación e instala lo
necesario (hace falta internet). Además, crea en tu escritorio el ícono
**Texto a MP3**. A partir de entonces, abre la aplicación con doble clic en ese
ícono: se abre en su ventana, sin navegador y sin ventana negra.

Si mueves la carpeta a otro sitio, vuelve a hacer doble clic en
`Abrir Texto a MP3 (Windows).bat` para que el ícono apunte al lugar nuevo.

## Mac

Haz doble clic en `Abrir Texto a MP3 (Mac).command`. La primera vez macOS puede
bloquearlo: haz clic derecho sobre el archivo, elige **Abrir** y confirma.

## Cómo se usa

1. Escribe o pega el texto (o pulsa **Abrir archivo .txt…**).
2. Elige el idioma y, si quieres, **Leer más despacio**.
3. Pulsa **Convertir y guardar MP3…** y elige dónde guardarlo.
4. Pulsa **Escuchar** para oírlo o **Abrir carpeta** para ver el archivo.

## Instalación manual

Si prefieres usar la terminal, instala la librería de voz y abre la ventana:

```bash
pip install -r requirements.txt
python texto_a_mp3.py
```

Si prefieres la versión en el navegador: `python texto_a_mp3.py --web`.

## Uso desde la terminal

```bash
# Texto directo
python texto_a_mp3.py "Hola, ¿qué tal?" -o saludo.mp3

# Desde un archivo de texto (crea cuento.mp3)
python texto_a_mp3.py -a cuento.txt

# Otro idioma y más despacio
python texto_a_mp3.py "Good morning" -l en --lento

# Ver todos los idiomas disponibles
python texto_a_mp3.py --idiomas
```

| Opción | Qué hace |
| --- | --- |
| `-a ARCHIVO` | Lee el texto desde un archivo `.txt` |
| `-o SALIDA` | Nombre del MP3 (por defecto `salida.mp3`, o el nombre del `.txt`) |
| `-l IDIOMA` | Código de idioma: `es`, `en`, `pt`, `fr`… (por defecto `es`) |
| `--lento` | Lee más despacio |
| `-m offline` | Usa las voces del sistema, sin internet |
| `--web` | Abre la versión en el navegador |

## Motores de voz

- **google** (por defecto): voz natural. Necesita conexión a internet.
- **offline**: usa las voces instaladas en tu ordenador y funciona sin
  internet. La voz suena más robótica. Necesita dos cosas más:
  - `pip install pyttsx3`
  - [ffmpeg](https://ffmpeg.org/download.html) instalado (en Windows:
    `winget install ffmpeg`; en macOS: `brew install ffmpeg`; en Linux:
    `sudo apt install ffmpeg espeak-ng`).

## Pruebas

```bash
python -m unittest -v
```
