Hello World!
Este es mi primer cambio en GitHub

# Texto a MP3

Aplicación sencilla en Python que convierte cualquier texto, o un **PDF
completo**, en un archivo de audio **MP3** que puedes escuchar sin internet.
Se abre en su propia ventana, como cualquier programa, y también se puede usar
desde la terminal.

- **Voz natural sin internet** (Piper). Cada voz se descarga una sola vez
  (unos 60 MB) y queda guardada en la carpeta `voces`. A partir de ahí la
  conversión ya no necesita conexión.
- **Medidor de avance**: la barra muestra el porcentaje convertido y el tiempo
  que falta. En el cuadro de texto, lo ya convertido se pinta de verde y el
  trozo en curso, de amarillo. El botón rojo **Detener** para en cualquier
  momento.
- **PDF**: quita los números de página, los encabezados, las notas al pie y sus
  llamadas (¹, ²), y une las palabras partidas con guion. Si el PDF tiene más
  de 20 páginas, pregunta de cuál a cuál quieres convertir.

## Instalarla en Windows (con ícono en el escritorio)

1. Instala [Python 3](https://www.python.org/downloads/) (3.9 o más reciente).
   Al instalar, marca la casilla **"Add python.exe to PATH"**.
2. Descarga la carpeta de la aplicación y guárdala donde quieras (por ejemplo,
   en **Documentos**).
3. Abre la carpeta y haz doble clic en `Abrir Texto a MP3 (Windows).bat`.

La primera vez tarda unos minutos, porque prepara la aplicación e instala lo
necesario (hace falta internet). Además, crea en tu escritorio el ícono
**Texto a MP3**. A partir de entonces, abre la aplicación con doble clic en ese
ícono: se abre en su ventana, sin navegador y sin ventana negra.

Si mueves la carpeta a otro sitio, vuelve a hacer doble clic en
`Abrir Texto a MP3 (Windows).bat` para que el ícono apunte al lugar nuevo.

## Mac

Haz doble clic en `Abrir Texto a MP3 (Mac).command`. La primera vez macOS puede
bloquearlo: haz clic derecho sobre el archivo, elige **Abrir** y confirma.

## Cómo se usa

1. Escribe o pega el texto, o pulsa **Abrir .txt o PDF…**.
2. Elige el motor (**Sin internet** o **Google**), la voz y, si quieres,
   **Leer más despacio**.
3. Pulsa **Convertir y guardar MP3…** y elige dónde guardarlo.
4. Pulsa **Escuchar** para oírlo o **Abrir carpeta** para ver el archivo.

Mientras convierte, el MP3 se va escribiendo como `nombre.mp3.parcial`.
Solo recibe su nombre final cuando termina bien, así nunca queda un MP3 a
medias.

## Voces sin internet

| Voz | Para qué |
| --- | --- |
| `es_MX-claude-high` | Español de México, la más natural (predeterminada) |
| `es_MX-ald-medium` | Español de México, casi el doble de rápida al convertir |
| `es_ES-davefx-medium` | Español de España |
| `es_AR-daniela-high` | Español de Argentina |
| `en_US-lessac-medium`, `pt_BR-faber-medium`, `fr_FR-siwis-medium`, `it_IT-paola-medium`, `de_DE-thorsten-medium`, `ca_ES-upc_ona-medium` | Inglés, portugués, francés, italiano, alemán y catalán |

Medido en una computadora con un procesador AMD FX-6100, la voz Claude
convierte unos 38 caracteres por segundo y la voz Ald, unos 65. Un PDF de
80 000 caracteres (unos 90 minutos de audio) tarda entre 20 y 35 minutos en
convertirse.

## Instalación manual

Si prefieres usar la terminal, instala las librerías y abre la ventana:

```bash
pip install -r requirements.txt
python texto_a_mp3.py
```

Si prefieres la versión en el navegador: `python texto_a_mp3.py --web`.

## Uso desde la terminal

```bash
# Texto directo (sin internet, voz natural)
python texto_a_mp3.py "Hola, ¿qué tal?" -o saludo.mp3

# Un PDF completo (crea libro.mp3) o solo unas páginas
python texto_a_mp3.py -a libro.pdf
python texto_a_mp3.py -a libro.pdf -p 15-42

# Otra voz, o la voz de Google en otro idioma y más despacio
python texto_a_mp3.py -a cuento.txt -v es_MX-ald-medium
python texto_a_mp3.py "Good morning" -m google -l en --lento

# Ver las voces sin internet y los idiomas de Google
python texto_a_mp3.py --voces
python texto_a_mp3.py --idiomas
```

| Opción | Qué hace |
| --- | --- |
| `-a ARCHIVO` | Lee el texto desde un archivo `.txt` o `.pdf` |
| `-p DESDE-HASTA` | Con un PDF, lee solo esas páginas |
| `-o SALIDA` | Nombre del MP3 (por defecto `salida.mp3`, o el nombre del archivo) |
| `-m MOTOR` | `offline` (sin internet, por defecto) o `google` |
| `-v VOZ` | Voz sin internet (ver `--voces`) |
| `-l IDIOMA` | Código de idioma: `es`, `en`, `pt`, `fr`… (por defecto `es`) |
| `--lento` | Lee más despacio |
| `--web` | Abre la versión en el navegador |

## Si el PDF es un escaneo

La app lee el texto que trae el PDF; no reconoce letras en imágenes. Si el
PDF son fotos de páginas sin texto, avisa. Si es un escaneo con un
reconocimiento de texto (OCR) de mala calidad, la voz leerá esos mismos
errores (por ejemplo, «m altrato» en vez de «maltrato»).

## Pruebas

```bash
python -m unittest -v
```
