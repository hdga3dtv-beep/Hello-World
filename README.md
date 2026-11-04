Hello World!
Este es mi primer cambio en GitHub

# Texto a MP3

Aplicación sencilla en Python que convierte cualquier texto en un archivo de
audio **MP3**. Se puede usar desde el navegador o desde la terminal.

## Instalación

1. Instala [Python 3](https://www.python.org/downloads/) (3.8 o más reciente).
2. Instala la librería de voz:

   ```bash
   pip install -r requirements.txt
   ```

## Uso desde el navegador (lo más fácil)

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
