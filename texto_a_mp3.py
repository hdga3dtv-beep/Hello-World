#!/usr/bin/env python3
"""Texto a MP3: convierte cualquier texto en un archivo de audio MP3.

Uso rápido:
    python texto_a_mp3.py "Hola, mundo" -o hola.mp3
    python texto_a_mp3.py -a cuento.txt              # crea cuento.mp3
    python texto_a_mp3.py --web                      # interfaz en el navegador

Motores de voz:
    google   (por defecto) Voz natural de Google. Necesita internet y la
             librería gTTS:  pip install gTTS
    offline  Usa las voces instaladas en tu sistema, sin internet. Necesita
             pyttsx3 (pip install pyttsx3) y ffmpeg instalado.
"""

import argparse
import concurrent.futures
import contextlib
import html
import io
import json
import multiprocessing
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MOTORES = ("google", "offline")

# Idiomas que se muestran en la interfaz web. Desde la línea de comandos se
# puede usar cualquier código que admita el motor (ver --idiomas).
IDIOMAS = {
    "es": "Español",
    "en": "Inglés",
    "pt": "Portugués",
    "fr": "Francés",
    "it": "Italiano",
    "de": "Alemán",
    "ca": "Catalán",
    "ja": "Japonés",
    "zh-CN": "Chino",
}

# Nombre del idioma en inglés, para encontrar voces del sistema como
# "Microsoft Sabina Desktop - Spanish (Mexico)" en Windows.
_NOMBRES_EN = {
    "es": "spanish",
    "en": "english",
    "pt": "portuguese",
    "fr": "french",
    "it": "italian",
    "de": "german",
    "ca": "catalan",
    "ja": "japanese",
    "zh": "chinese",
}

LIMITE_PETICION = 1_000_000  # bytes máximos aceptados por la interfaz web


class ErrorConversion(Exception):
    """Error con un mensaje pensado para mostrarse directamente al usuario."""


# --------------------------------------------------------------------------
# Conversión
# --------------------------------------------------------------------------

def generar_mp3(texto, idioma="es", lento=False, motor="google"):
    """Convierte ``texto`` en audio y devuelve los bytes del MP3."""
    texto = (texto or "").strip()
    if not texto:
        raise ErrorConversion("No hay texto para convertir.")
    if motor not in MOTORES:
        raise ErrorConversion(
            f"Motor desconocido: {motor!r}. Usa uno de: {', '.join(MOTORES)}."
        )

    with tempfile.TemporaryDirectory() as carpeta:
        mp3 = os.path.join(carpeta, "audio.mp3")
        if motor == "google":
            _mp3_con_google(texto, mp3, idioma, lento)
        else:
            _mp3_offline(texto, mp3, idioma, lento, carpeta)
        with open(mp3, "rb") as f:
            return f.read()


def convertir(texto, salida, idioma="es", lento=False, motor="google"):
    """Convierte ``texto`` y lo guarda en el archivo MP3 ``salida``.

    Devuelve la ruta absoluta del archivo creado. El archivo solo se escribe
    si la conversión termina bien, así nunca queda un MP3 a medias.
    """
    audio = generar_mp3(texto, idioma=idioma, lento=lento, motor=motor)
    salida = os.path.abspath(salida)
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    with open(salida, "wb") as f:
        f.write(audio)
    return salida


def _mp3_con_google(texto, ruta_mp3, idioma, lento):
    try:
        from gtts import gTTS
        from gtts.tts import gTTSError
    except ImportError:
        raise ErrorConversion(
            "Falta la librería gTTS. Instálala con:  pip install gTTS"
        ) from None

    try:
        gTTS(texto, lang=idioma, slow=lento).save(ruta_mp3)
    except ValueError as e:  # gTTS lanza ValueError si el idioma no existe
        raise ErrorConversion(
            f"Google no admite el idioma {idioma!r}. "
            "Usa --idiomas para ver la lista."
        ) from e
    except gTTSError as e:
        raise ErrorConversion(
            "No se pudo conectar con el servicio de voz de Google. Revisa tu "
            "conexión a internet o usa el motor sin internet ('offline'). "
            f"(Detalle: {e})"
        ) from e


def _mp3_offline(texto, ruta_mp3, idioma, lento, carpeta):
    try:
        import pyttsx3  # noqa: F401  (solo comprobamos que esté instalado)
    except ImportError:
        raise ErrorConversion(
            "El motor offline necesita pyttsx3. Instálalo con:  pip install pyttsx3"
        ) from None
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise ErrorConversion(
            "El motor offline necesita ffmpeg para crear el MP3. "
            "Descárgalo desde https://ffmpeg.org/download.html"
        )

    ruta_wav = os.path.join(carpeta, "voz.wav")
    # pyttsx3 da problemas si se usa varias veces o desde hilos (como hace la
    # interfaz web), así que cada síntesis se hace en un proceso nuevo.
    contexto = multiprocessing.get_context("spawn")
    with concurrent.futures.ProcessPoolExecutor(1, mp_context=contexto) as ex:
        ex.submit(_sintetizar_wav, texto, ruta_wav, idioma, lento).result()

    if not os.path.exists(ruta_wav) or os.path.getsize(ruta_wav) == 0:
        raise ErrorConversion("El motor de voz del sistema no generó audio.")

    resultado = subprocess.run(
        [ffmpeg, "-y", "-loglevel", "error", "-i", ruta_wav,
         "-codec:a", "libmp3lame", "-q:a", "4", ruta_mp3],
        capture_output=True, text=True,
    )
    if resultado.returncode != 0:
        raise ErrorConversion(
            f"ffmpeg no pudo crear el MP3: {resultado.stderr.strip()}"
        )


def _sintetizar_wav(texto, ruta_wav, idioma, lento):
    """Se ejecuta en un proceso aparte: genera un WAV con pyttsx3."""
    import pyttsx3

    # pyttsx3 imprime mensajes propios; los silenciamos.
    with contextlib.redirect_stdout(io.StringIO()):
        motor = pyttsx3.init()
        voz = _buscar_voz(motor.getProperty("voices"), idioma)
        if voz is not None:
            motor.setProperty("voice", voz)
        if lento:
            motor.setProperty("rate", int(motor.getProperty("rate") * 0.7))
        motor.save_to_file(texto, ruta_wav)
        motor.runAndWait()


def _buscar_voz(voces, idioma):
    """Devuelve el id de la voz del sistema que mejor encaja con ``idioma``."""
    idioma = idioma.lower().replace("_", "-")
    base = idioma.split("-")[0]
    nombre_en = _NOMBRES_EN.get(base)

    def idiomas_de(voz):
        for lang in getattr(voz, "languages", None) or []:
            if isinstance(lang, bytes):
                lang = lang.decode("utf-8", "ignore")
            yield str(lang).strip("\x05 ").lower().replace("_", "-")

    candidatas = []
    for voz in voces:
        langs = list(idiomas_de(voz))
        vid = str(voz.id or "").lower()
        nombre = str(voz.name or "").lower()
        if idioma in langs or vid.endswith("/" + idioma):
            puntos = 3
        elif any(l.split("-")[0] == base for l in langs) or vid.endswith("/" + base):
            puntos = 2
        elif nombre_en and nombre_en in nombre:
            puntos = 1
        else:
            continue
        candidatas.append((puntos, voz.id))

    if not candidatas:
        return None
    return max(candidatas, key=lambda c: c[0])[1]


def leer_archivo(ruta):
    """Lee un archivo de texto en UTF-8 (o Latin-1 si no es UTF-8)."""
    try:
        with open(ruta, encoding="utf-8-sig") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(ruta, encoding="latin-1") as f:
            return f.read()
    except OSError as e:
        raise ErrorConversion(f"No se pudo leer {ruta!r}: {e.strerror}") from e


# --------------------------------------------------------------------------
# Interfaz web
# --------------------------------------------------------------------------

PAGINA_HTML = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Texto a MP3</title>
<style>
  :root {
    --fondo: #f5f6f8; --tarjeta: #ffffff; --texto: #1d2330; --suave: #5b6475;
    --borde: #d8dce4; --acento: #2f6fed; --acento-hover: #2459c4;
    --sobre-acento: #ffffff; --error: #b3261e; --error-fondo: #fdeceb;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --fondo: #12151b; --tarjeta: #1b2029; --texto: #e7eaf0; --suave: #9aa3b2;
      --borde: #2e3542; --acento: #7aa2ff; --acento-hover: #9bb9ff;
      --sobre-acento: #0b1220; --error: #ffb4ab; --error-fondo: #3b1f21;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--fondo); color: var(--texto); line-height: 1.5;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  main { max-width: 720px; margin: 0 auto; padding: 40px 16px 56px; }
  h1 { margin: 0 0 4px; font-size: 1.75rem; }
  .sub { margin: 0 0 24px; color: var(--suave); }
  .tarjeta {
    background: var(--tarjeta); border: 1px solid var(--borde);
    border-radius: 12px; padding: 20px;
  }
  label { font-weight: 600; font-size: .9rem; }
  textarea, select {
    width: 100%; margin-top: 6px; font: inherit; color: inherit;
    background: var(--tarjeta); border: 1px solid var(--borde); border-radius: 8px;
  }
  textarea { min-height: 200px; resize: vertical; padding: 12px; }
  select { padding: 8px 10px; }
  textarea:focus, select:focus, button:focus-visible {
    outline: 2px solid var(--acento); outline-offset: 1px;
  }
  .contador { text-align: right; color: var(--suave); font-size: .8rem; margin-top: 4px; }
  .opciones {
    display: grid; gap: 16px; margin: 12px 0 20px; align-items: end;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  }
  .check { display: flex; gap: 8px; align-items: center; font-weight: 400; padding-bottom: 9px; }
  .check input { width: 18px; height: 18px; margin: 0; }
  button {
    width: 100%; padding: 12px; font: inherit; font-weight: 600; border: 0;
    border-radius: 8px; cursor: pointer; color: var(--sobre-acento); background: var(--acento);
  }
  button:hover { background: var(--acento-hover); }
  button:disabled { opacity: .65; cursor: progress; }
  .error {
    display: none; margin-top: 16px; padding: 12px; border-radius: 8px;
    background: var(--error-fondo); color: var(--error);
  }
  .resultado { display: none; margin-top: 20px; }
  audio { width: 100%; }
  .descargar { display: inline-block; margin-top: 10px; color: var(--acento); font-weight: 600; }
  .nota { color: var(--suave); font-size: .85rem; margin-top: 20px; }
  kbd {
    font: .8rem ui-monospace, monospace; padding: 1px 5px;
    border: 1px solid var(--borde); border-radius: 4px;
  }
</style>
</head>
<body>
<main>
  <h1>Texto a MP3</h1>
  <p class="sub">Escribe o pega un texto y conviértelo en un archivo de audio.</p>

  <div class="tarjeta">
    <label for="texto">Texto</label>
    <textarea id="texto" placeholder="Hola, este texto se convertirá en audio..."></textarea>
    <div class="contador" id="contador">0 caracteres</div>

    <div class="opciones">
      <div>
        <label for="idioma">Idioma</label>
        <select id="idioma">{{OPCIONES_IDIOMA}}</select>
      </div>
      <div>
        <label for="motor">Motor de voz</label>
        <select id="motor">
          <option value="google">Google (con internet)</option>
          <option value="offline">Sistema (sin internet)</option>
        </select>
      </div>
      <label class="check"><input type="checkbox" id="lento"> Leer más despacio</label>
    </div>

    <button id="convertir">Convertir a MP3</button>
    <div class="error" id="error" role="alert"></div>

    <div class="resultado" id="resultado">
      <audio id="audio" controls></audio>
      <a class="descargar" id="descargar" href="#">Descargar MP3</a>
    </div>
  </div>

  <p class="nota">Atajo: <kbd>Ctrl</kbd> + <kbd>Enter</kbd> para convertir.
  Para cerrar la aplicación, pulsa <kbd>Ctrl</kbd> + <kbd>C</kbd> en la terminal.</p>
</main>

<script>
  const $ = (id) => document.getElementById(id);
  const texto = $("texto"), boton = $("convertir"), error = $("error");
  const resultado = $("resultado"), audio = $("audio"), descargar = $("descargar");
  let urlAnterior = null;

  texto.addEventListener("input", () => {
    const n = texto.value.length;
    $("contador").textContent = n + (n === 1 ? " carácter" : " caracteres");
  });
  texto.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) boton.click();
  });

  function nombreArchivo(t) {
    const base = t.trim().split(/\\s+/).slice(0, 5).join(" ")
      .normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase()
      .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
    return (base || "audio") + ".mp3";
  }

  function mostrarError(msg) {
    error.textContent = msg;
    error.style.display = "block";
  }

  boton.addEventListener("click", async () => {
    error.style.display = "none";
    if (!texto.value.trim()) { mostrarError("Escribe algún texto primero."); return; }
    boton.disabled = true;
    boton.textContent = "Convirtiendo…";
    try {
      const r = await fetch("/convertir", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          texto: texto.value, idioma: $("idioma").value,
          motor: $("motor").value, lento: $("lento").checked,
        }),
      });
      if (!r.ok) {
        let msg = "Error " + r.status;
        try { msg = (await r.json()).error || msg; } catch (_) {}
        throw new Error(msg);
      }
      const blob = await r.blob();
      if (urlAnterior) URL.revokeObjectURL(urlAnterior);
      urlAnterior = URL.createObjectURL(blob);
      audio.src = urlAnterior;
      descargar.href = urlAnterior;
      descargar.download = nombreArchivo(texto.value);
      descargar.textContent = "Descargar " + descargar.download;
      resultado.style.display = "block";
      audio.play().catch(() => {});
    } catch (e) {
      mostrarError(e instanceof TypeError
        ? "No se pudo contactar con la aplicación. ¿Sigue abierta la terminal?"
        : e.message);
    } finally {
      boton.disabled = false;
      boton.textContent = "Convertir a MP3";
    }
  });
</script>
</body>
</html>
"""


def _pagina():
    opciones = "".join(
        f'<option value="{html.escape(codigo)}">{html.escape(nombre)}</option>'
        for codigo, nombre in IDIOMAS.items()
    )
    return PAGINA_HTML.replace("{{OPCIONES_IDIOMA}}", opciones)


class _Manejador(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._responder(200, _pagina().encode("utf-8"), "text/html; charset=utf-8")
        else:
            self._responder_json(404, {"error": "Página no encontrada."})

    def do_POST(self):
        if self.path != "/convertir":
            return self._responder_json(404, {"error": "Página no encontrada."})
        # Exigir JSON obliga al navegador a pedir permiso (CORS) si otra web
        # intenta usar esta aplicación local.
        if not self.headers.get("Content-Type", "").startswith("application/json"):
            return self._responder_json(415, {"error": "Se esperaba JSON."})
        try:
            largo = int(self.headers.get("Content-Length", 0))
        except ValueError:
            largo = 0
        if largo <= 0:
            return self._responder_json(400, {"error": "Petición vacía."})
        if largo > LIMITE_PETICION:
            return self._responder_json(413, {"error": "El texto es demasiado largo."})

        try:
            datos = json.loads(self.rfile.read(largo).decode("utf-8"))
            if not isinstance(datos, dict):
                raise ValueError
        except (ValueError, UnicodeDecodeError):
            return self._responder_json(400, {"error": "Petición no válida."})

        try:
            audio = generar_mp3(
                str(datos.get("texto") or ""),
                idioma=str(datos.get("idioma") or "es"),
                lento=bool(datos.get("lento")),
                motor=str(datos.get("motor") or "google"),
            )
        except ErrorConversion as e:
            return self._responder_json(400, {"error": str(e)})
        except Exception as e:  # cualquier otro fallo se muestra en la página
            return self._responder_json(500, {"error": f"Error inesperado: {e}"})
        self._responder(200, audio, "audio/mpeg")

    def _responder(self, codigo, cuerpo, tipo):
        self.send_response(codigo)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(cuerpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(cuerpo)

    def _responder_json(self, codigo, datos):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self._responder(codigo, cuerpo, "application/json; charset=utf-8")

    def log_message(self, formato, *args):
        pass  # no llenar la terminal con cada petición


def crear_servidor(puerto=8000):
    """Crea el servidor web local (solo accesible desde este equipo)."""
    try:
        return ThreadingHTTPServer(("127.0.0.1", puerto), _Manejador)
    except OSError:
        # El puerto está ocupado: dejamos que el sistema elija uno libre.
        return ThreadingHTTPServer(("127.0.0.1", 0), _Manejador)


def iniciar_web(puerto=8000, abrir_navegador=True):
    servidor = crear_servidor(puerto)
    url = f"http://127.0.0.1:{servidor.server_address[1]}/"
    print(f"Texto a MP3 está listo en {url}")
    print("Pulsa Ctrl+C para cerrar la aplicación.")
    if abrir_navegador:
        threading.Timer(0.5, webbrowser.open, args=(url,)).start()
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nHasta luego.")
    finally:
        servidor.server_close()


# --------------------------------------------------------------------------
# Línea de comandos
# --------------------------------------------------------------------------

EJEMPLOS = """ejemplos:
  python texto_a_mp3.py "Hola, ¿qué tal?" -o saludo.mp3
  python texto_a_mp3.py -a cuento.txt                 (crea cuento.mp3)
  python texto_a_mp3.py "Good morning" -l en --lento
  python texto_a_mp3.py "Sin internet" -m offline
  python texto_a_mp3.py --web                         (abre el navegador)

Si lo ejecutas sin texto, se abre la interfaz en el navegador.
"""


def _crear_parser():
    p = argparse.ArgumentParser(
        prog="texto_a_mp3",
        description="Convierte texto en un archivo de audio MP3.",
        epilog=EJEMPLOS,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("texto", nargs="*", help="texto a convertir")
    p.add_argument("-a", "--archivo", help="leer el texto desde un archivo .txt")
    p.add_argument("-o", "--salida",
                   help="archivo MP3 de salida (por defecto: salida.mp3, "
                        "o el nombre del archivo de texto con .mp3)")
    p.add_argument("-l", "--idioma", default="es",
                   help="código de idioma: es, en, pt, fr... (por defecto: es)")
    p.add_argument("-m", "--motor", choices=MOTORES, default="google",
                   help="google (con internet, por defecto) u offline (voces del sistema)")
    p.add_argument("--lento", action="store_true", help="leer más despacio")
    p.add_argument("--web", action="store_true", help="abrir la interfaz en el navegador")
    p.add_argument("--puerto", type=int, default=8000,
                   help="puerto de la interfaz web (por defecto: 8000)")
    p.add_argument("--no-abrir", action="store_true",
                   help="con --web, no abrir el navegador automáticamente")
    p.add_argument("--idiomas", action="store_true",
                   help="mostrar los idiomas que admite Google y salir")
    return p


def _nombre_salida(args):
    if args.salida:
        salida = args.salida
    elif args.archivo:
        salida = os.path.splitext(args.archivo)[0] + ".mp3"
    else:
        salida = "salida.mp3"
    if not salida.lower().endswith(".mp3"):
        salida += ".mp3"
    return salida


def _mostrar_idiomas():
    try:
        from gtts.lang import tts_langs
    except ImportError:
        raise ErrorConversion("Falta la librería gTTS. Instálala con:  pip install gTTS") from None
    for codigo, nombre in sorted(tts_langs().items()):
        print(f"  {codigo:<8} {nombre}")


def main(argv=None):
    parser = _crear_parser()
    args = parser.parse_args(argv)

    try:
        if args.idiomas:
            _mostrar_idiomas()
            return 0

        if args.archivo and args.texto:
            parser.error("usa un texto o --archivo, pero no ambos a la vez")

        sin_texto = not (args.archivo or args.texto)
        if args.web or (sin_texto and (sys.stdin is None or sys.stdin.isatty())):
            iniciar_web(args.puerto, abrir_navegador=not args.no_abrir)
            return 0

        if args.archivo:
            texto = leer_archivo(args.archivo)
        elif args.texto:
            texto = " ".join(args.texto)
        else:  # texto recibido por una tubería:  echo "hola" | python texto_a_mp3.py
            texto = sys.stdin.read()

        print(f"Convirtiendo con el motor '{args.motor}' (idioma: {args.idioma})...")
        ruta = convertir(texto, _nombre_salida(args), idioma=args.idioma,
                         lento=args.lento, motor=args.motor)
        tam_kb = os.path.getsize(ruta) / 1024
        print(f"Listo: {ruta} ({tam_kb:.1f} KB)")
        return 0
    except ErrorConversion as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
