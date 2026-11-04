Hello World!
Este es mi primer cambio en GitHub

# Texto a MP3

Aplicación sencilla en Python que convierte cualquier texto en un archivo de
audio **MP3**. Se puede usar desde el navegador o desde la terminal.

## Ponerla en el escritorio (doble clic)

1. Instala [Python 3](https://www.python.org/downloads/) (3.8 o más reciente).
   En Windows, marca la casilla **"Add python.exe to PATH"** al instalar.
2. Descarga la carpeta de la aplicación y déjala en tu escritorio.
3. Abre la carpeta y haz doble clic en:
   - **Windows:** `Abrir Texto a MP3 (Windows).bat`
   - **Mac:** `Abrir Texto a MP3 (Mac).command`. La primera vez macOS puede
     bloquearlo: haz clic derecho sobre el archivo, elige **Abrir** y
     confirma.

La primera vez tarda un poco, porque prepara la aplicación e instala lo
necesario (hace falta internet). Después se abre directamente en el navegador.
No cierres la ventana negra mientras uses la aplicación: al cerrarla, la
aplicación se apaga.

## Instalación manual

Si prefieres usar la terminal, instala la librería de voz:

```bash
pip install -r requirements.txt
```

## Uso desde el navegador

```bash
python texto_a_mp3.py
```

Se abre una página en tu navegador. Escribe o pega el texto, elige el idioma y
pulsa **Convertir a MP3**. Puedes escuchar el resultado ahí mismo y descargarlo.
Para cerrar la aplicación, pulsa `Ctrl + C` en la terminal.

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
| `--web` | Abre la interfaz en el navegador |

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
