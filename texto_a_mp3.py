#!/usr/bin/env python3
"""Texto a MP3: convierte cualquier texto en un archivo de audio MP3.

Uso rápido:
    python texto_a_mp3.py                            # abre la ventana de la app
    python texto_a_mp3.py "Hola, mundo" -o hola.mp3
    python texto_a_mp3.py -a cuento.txt              # crea cuento.mp3
    python texto_a_mp3.py --web                      # versión en el navegador

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
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import unicodedata
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
            f"El motor offline necesita pyttsx3. Instálalo con:  {_comando_pip('pyttsx3')}"
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
        # En Windows, evita que aparezca una ventana negra desde la app.
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    if resultado.returncode != 0:
        raise ErrorConversion(
            f"ffmpeg no pudo crear el MP3: {resultado.stderr.strip()}"
        )


def _comando_pip(paquete):
    """Comando para instalar ``paquete`` en el Python que ejecuta la app."""
    if sys.prefix != sys.base_prefix:  # entorno propio (p. ej. el del lanzador)
        return f'"{sys.executable}" -m pip install {paquete}'
    return f"pip install {paquete}"


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
# Ventana de escritorio (como cualquier programa, sin navegador)
# --------------------------------------------------------------------------

CARPETA_APP = os.path.dirname(os.path.abspath(__file__))
ICONO = os.path.join(CARPETA_APP, "icono.ico")
NOMBRES_MOTOR = {"google": "Google (con internet)", "offline": "Sistema (sin internet)"}
_COLOR_SUAVE, _COLOR_ERROR, _COLOR_EXITO = "#5b6475", "#b3261e", "#1e7b34"


def nombre_sugerido(texto):
    """Nombre de archivo a partir de las primeras palabras: 'hola-mundo.mp3'."""
    sin_tildes = unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode()
    palabras = sin_tildes.lower().split()[:5]
    base = re.sub(r"[^a-z0-9]+", "-", " ".join(palabras)).strip("-")
    return (base or "audio") + ".mp3"


def _carpeta_inicial():
    """Carpeta donde se propone guardar: Música, si existe; si no, Documentos."""
    inicio = os.path.expanduser("~")
    for nombre in ("Music", "Documents"):
        ruta = os.path.join(inicio, nombre)
        if os.path.isdir(ruta):
            return ruta
    return inicio


def _abrir_con_sistema(ruta, mostrar_en_carpeta=False):
    """Abre un archivo con su programa (o muestra la carpeta que lo contiene)."""
    if sys.platform == "win32":
        if mostrar_en_carpeta:
            subprocess.Popen(f'explorer /select,"{os.path.normpath(ruta)}"')
        else:
            os.startfile(ruta)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", "-R", ruta] if mostrar_en_carpeta else ["open", ruta])
    else:
        subprocess.Popen(["xdg-open", os.path.dirname(ruta) if mostrar_en_carpeta else ruta])


class VentanaApp:
    """Ventana principal de la aplicación, hecha con tkinter."""

    def __init__(self, raiz):
        import tkinter as tk
        from tkinter import font as tkfont
        from tkinter import ttk

        self.raiz = raiz
        self.ultimo_mp3 = None
        self.carpeta_guardado = _carpeta_inicial()
        self._nombre_desde_txt = None
        self._resultado = None
        self._ocupada = False

        raiz.title("Texto a MP3")
        escala = raiz.winfo_fpixels("1i") / 96  # pantallas con zoom (125 %, 150 %...)
        raiz.geometry(f"{int(720 * escala)}x{int(600 * escala)}")
        raiz.minsize(int(560 * escala), int(460 * escala))
        if sys.platform == "win32" and os.path.exists(ICONO):
            try:
                raiz.iconbitmap(default=ICONO)
            except tk.TclError:
                pass
        raiz.report_callback_exception = self._error_inesperado

        estilo = ttk.Style(raiz)
        for tema in ("vista", "aqua", "clam"):
            if tema in estilo.theme_names():
                estilo.theme_use(tema)
                break
        familia = tkfont.nametofont("TkDefaultFont").actual("family")
        estilo.configure("TLabel", font=(familia, 10))
        estilo.configure("TCheckbutton", font=(familia, 10))
        estilo.configure("TButton", font=(familia, 10), padding=(10, 6))

        marco = ttk.Frame(raiz, padding=(24, 18))
        marco.pack(fill="both", expand=True)
        marco.columnconfigure(0, weight=1)
        marco.rowconfigure(2, weight=1)

        ttk.Label(marco, text="Texto a MP3", font=(familia, 18, "bold")).grid(
            row=0, column=0, sticky="w")
        cabecera = ttk.Frame(marco)
        cabecera.grid(row=1, column=0, sticky="ew", pady=(2, 8))
        ttk.Label(cabecera, text="Escribe o pega el texto que quieres convertir en audio:",
                  foreground=_COLOR_SUAVE).pack(side="left")
        ttk.Button(cabecera, text="Abrir archivo .txt…", command=self.abrir_txt).pack(side="right")

        caja = ttk.Frame(marco)
        caja.grid(row=2, column=0, sticky="nsew")
        caja.columnconfigure(0, weight=1)
        caja.rowconfigure(0, weight=1)
        self.texto = tk.Text(caja, wrap="word", undo=True, font=(familia, 12),
                             relief="solid", borderwidth=1, padx=10, pady=8,
                             highlightthickness=0)
        barra = ttk.Scrollbar(caja, orient="vertical", command=self.texto.yview)
        self.texto.configure(yscrollcommand=barra.set)
        self.texto.grid(row=0, column=0, sticky="nsew")
        barra.grid(row=0, column=1, sticky="ns")

        self.contador = ttk.Label(marco, text="0 caracteres", foreground=_COLOR_SUAVE)
        self.contador.grid(row=3, column=0, sticky="e", pady=(4, 0))

        opciones = ttk.Frame(marco)
        opciones.grid(row=4, column=0, sticky="ew", pady=(6, 16))
        ttk.Label(opciones, text="Idioma").grid(row=0, column=0, sticky="w")
        ttk.Label(opciones, text="Motor de voz").grid(row=0, column=1, sticky="w", padx=(16, 0))
        self.idioma = ttk.Combobox(opciones, state="readonly", width=14,
                                   values=list(IDIOMAS.values()), font=(familia, 10))
        self.idioma.current(0)
        self.idioma.grid(row=1, column=0, sticky="w", pady=(3, 0))
        self.motor = ttk.Combobox(opciones, state="readonly", width=24,
                                  values=list(NOMBRES_MOTOR.values()), font=(familia, 10))
        self.motor.current(0)
        self.motor.grid(row=1, column=1, sticky="w", padx=(16, 0), pady=(3, 0))
        self.lento = tk.BooleanVar(value=False)
        ttk.Checkbutton(opciones, text="Leer más despacio", variable=self.lento).grid(
            row=1, column=2, sticky="w", padx=(20, 0), pady=(3, 0))

        botones = ttk.Frame(marco)
        botones.grid(row=5, column=0, sticky="ew")
        botones.columnconfigure(0, weight=1)
        self.boton = tk.Button(
            botones, text="Convertir y guardar MP3…", command=self.convertir_y_guardar,
            font=(familia, 12, "bold"), bg="#2f6fed", fg="white",
            activebackground="#2459c4", activeforeground="white",
            disabledforeground="#dfe7ff", relief="flat", borderwidth=0,
            cursor="hand2", padx=12, pady=9)
        self.boton.grid(row=0, column=0, sticky="ew")
        self.boton_escuchar = ttk.Button(botones, text="▶  Escuchar",
                                         command=self.escuchar, state="disabled")
        self.boton_escuchar.grid(row=0, column=1, sticky="ns", padx=(10, 0))
        self.boton_carpeta = ttk.Button(botones, text="Abrir carpeta",
                                        command=self.abrir_carpeta, state="disabled")
        self.boton_carpeta.grid(row=0, column=2, sticky="ns", padx=(8, 0))

        self.progreso = ttk.Progressbar(marco, mode="indeterminate")
        self.progreso.grid(row=6, column=0, sticky="ew", pady=(14, 0))
        self.progreso.grid_remove()
        self.estado = ttk.Label(marco, justify="left")
        self.estado.grid(row=7, column=0, sticky="ew", pady=(12, 0))
        marco.bind("<Configure>",
                   lambda e: self.estado.configure(wraplength=max(200, e.width - 48)))
        self._mostrar_estado("Atajo: Ctrl + Enter para convertir.")

        self.texto.bind("<<Modified>>", self._al_modificar)
        self.texto.bind("<Control-a>", self._seleccionar_todo)
        self.texto.bind("<Control-Return>", self._atajo_convertir)
        raiz.bind("<Control-Return>", self._atajo_convertir)
        self.texto.focus_set()

    # --- acciones -------------------------------------------------------

    def abrir_txt(self):
        from tkinter import filedialog

        ruta = filedialog.askopenfilename(
            parent=self.raiz, title="Abrir archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if not ruta:
            return
        try:
            contenido = leer_archivo(ruta)
        except ErrorConversion as e:
            self._mostrar_estado(str(e), color=_COLOR_ERROR)
            return
        self.texto.delete("1.0", "end")
        self.texto.insert("1.0", contenido)
        self._nombre_desde_txt = os.path.splitext(os.path.basename(ruta))[0] + ".mp3"
        self._mostrar_estado(f"Texto cargado de «{os.path.basename(ruta)}».")

    def convertir_y_guardar(self):
        from tkinter import filedialog

        if self._ocupada:
            return
        texto = self.texto.get("1.0", "end-1c").strip()
        if not texto:
            self._mostrar_estado("Escribe algún texto primero.", color=_COLOR_ERROR)
            self.texto.focus_set()
            return
        ruta = filedialog.asksaveasfilename(
            parent=self.raiz, title="Guardar el audio como",
            defaultextension=".mp3", filetypes=[("Audio MP3", "*.mp3")],
            initialdir=self.carpeta_guardado,
            initialfile=self._nombre_desde_txt or nombre_sugerido(texto))
        if not ruta:
            return
        if not ruta.lower().endswith(".mp3"):
            ruta += ".mp3"
        self.carpeta_guardado = os.path.dirname(ruta)
        opciones = {
            "idioma": self._codigo(self.idioma.get(), IDIOMAS, "es"),
            "motor": self._codigo(self.motor.get(), NOMBRES_MOTOR, "google"),
            "lento": self.lento.get(),
        }
        self._ocupar(True)
        self._resultado = None
        threading.Thread(target=self._trabajar, args=(texto, ruta, opciones),
                         daemon=True).start()
        self.raiz.after(150, self._revisar)

    def escuchar(self):
        self._abrir(self.ultimo_mp3)

    def abrir_carpeta(self):
        self._abrir(self.ultimo_mp3, mostrar_en_carpeta=True)

    # --- detalles internos ----------------------------------------------

    def _trabajar(self, texto, ruta, opciones):
        # Se ejecuta en otro hilo para que la ventana no se congele.
        try:
            self._resultado = ("ok", convertir(texto, ruta, **opciones))
        except ErrorConversion as e:
            self._resultado = ("error", str(e))
        except Exception as e:
            self._resultado = ("error", f"Error inesperado: {e}")

    def _revisar(self):
        if self._resultado is None:
            self.raiz.after(150, self._revisar)
            return
        tipo, valor = self._resultado
        self._ocupar(False)
        if tipo == "ok":
            self.ultimo_mp3 = valor
            self.boton_escuchar.configure(state="normal")
            self.boton_carpeta.configure(state="normal")
            self._mostrar_estado(f"✔  Listo. Guardado en: {valor}", color=_COLOR_EXITO)
        else:
            self._mostrar_estado(valor, color=_COLOR_ERROR)

    def _ocupar(self, ocupada):
        self._ocupada = ocupada
        self.boton.configure(
            state="disabled" if ocupada else "normal",
            text="Convirtiendo…" if ocupada else "Convertir y guardar MP3…")
        if ocupada:
            self.progreso.grid()
            self.progreso.start(12)
            self._mostrar_estado("Convirtiendo… puede tardar unos segundos.")
        else:
            self.progreso.stop()
            self.progreso.grid_remove()

    def _abrir(self, ruta, mostrar_en_carpeta=False):
        if not ruta or not os.path.exists(ruta):
            self._mostrar_estado("No encuentro el archivo MP3. ¿Lo moviste o borraste?",
                                 color=_COLOR_ERROR)
            return
        try:
            _abrir_con_sistema(ruta, mostrar_en_carpeta)
        except OSError as e:
            self._mostrar_estado(f"No se pudo abrir: {e}", color=_COLOR_ERROR)

    def _mostrar_estado(self, mensaje, color=_COLOR_SUAVE):
        self.estado.configure(text=mensaje, foreground=color)

    def _al_modificar(self, _evento=None):
        n = len(self.texto.get("1.0", "end-1c"))
        self.contador.configure(text=f"{n} carácter" if n == 1 else f"{n} caracteres")
        self.texto.edit_modified(False)

    def _seleccionar_todo(self, _evento=None):
        self.texto.tag_add("sel", "1.0", "end-1c")
        return "break"

    def _atajo_convertir(self, _evento=None):
        self.convertir_y_guardar()
        return "break"

    @staticmethod
    def _codigo(nombre, tabla, defecto):
        return next((c for c, n in tabla.items() if n == nombre), defecto)

    def _error_inesperado(self, tipo, valor, rastro):
        from tkinter import messagebox

        messagebox.showerror("Texto a MP3", f"Ocurrió un error inesperado:\n\n{valor}",
                             parent=self.raiz)


def iniciar_ventana():
    """Abre la aplicación en su propia ventana (o la versión web si no se puede)."""
    try:
        import tkinter as tk
    except ImportError:
        print("Este Python no incluye tkinter (las ventanas). Abro la versión web.")
        return iniciar_web()
    if sys.platform == "win32":
        import ctypes
        try:  # que la barra de tareas muestre nuestro ícono y no el de Python
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("TextoAMP3")
        except Exception:
            pass
        try:  # texto nítido en pantallas con zoom
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass
    try:
        raiz = tk.Tk()
    except tk.TclError as e:
        print(f"No se pudo abrir la ventana ({e}). Abro la versión web.")
        return iniciar_web()
    VentanaApp(raiz)
    raiz.mainloop()


def _script_acceso_directo(programa, script, carpeta, icono=None):
    """Script de PowerShell que crea el ícono "Texto a MP3" en el escritorio.

    No usa comillas dobles para que pasarlo por la línea de comandos sea seguro.
    """
    def texto_ps(valor):
        return "'" + valor.replace("'", "''") + "'"

    lineas = [
        "$ErrorActionPreference = 'Stop'",
        "$escritorio = [Environment]::GetFolderPath('Desktop')",
        "$ruta = Join-Path $escritorio 'Texto a MP3.lnk'",
        "$acceso = (New-Object -ComObject WScript.Shell).CreateShortcut($ruta)",
        "$comilla = [string][char]34",
        f"$acceso.TargetPath = {texto_ps(programa)}",
        f"$acceso.Arguments = $comilla + {texto_ps(script)} + $comilla + ' --ventana'",
        f"$acceso.WorkingDirectory = {texto_ps(carpeta)}",
        "$acceso.Description = 'Convierte texto en audio MP3'",
    ]
    if icono:
        lineas.append(f"$acceso.IconLocation = {texto_ps(icono)}")
    lineas += ["$acceso.Save()", "Write-Output $ruta"]
    return "; ".join(lineas)


def crear_acceso_directo():
    """Crea (o actualiza) el ícono "Texto a MP3" en el escritorio de Windows.

    El ícono abre la ventana con pythonw.exe, así no aparece la ventana negra.
    """
    if sys.platform != "win32":
        raise ErrorConversion("Crear el ícono del escritorio solo funciona en Windows.")
    pythonw = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
    if not os.path.exists(pythonw):
        pythonw = sys.executable
    script = _script_acceso_directo(pythonw, os.path.abspath(__file__), CARPETA_APP,
                                    ICONO if os.path.exists(ICONO) else None)
    resultado = subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-Command", script],
        capture_output=True, text=True, errors="replace")
    if resultado.returncode != 0:
        raise ErrorConversion(
            f"No se pudo crear el ícono del escritorio: {resultado.stderr.strip()}")
    return resultado.stdout.strip()


# --------------------------------------------------------------------------
# Línea de comandos
# --------------------------------------------------------------------------

EJEMPLOS = """ejemplos:
  python texto_a_mp3.py "Hola, ¿qué tal?" -o saludo.mp3
  python texto_a_mp3.py -a cuento.txt                 (crea cuento.mp3)
  python texto_a_mp3.py "Good morning" -l en --lento
  python texto_a_mp3.py "Sin internet" -m offline
  python texto_a_mp3.py --web                         (versión en el navegador)

Si lo ejecutas sin texto, se abre la ventana de la aplicación.
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
    p.add_argument("--ventana", action="store_true",
                   help="abrir la aplicación en su ventana (lo normal sin texto)")
    p.add_argument("--web", action="store_true", help="abrir la versión en el navegador")
    p.add_argument("--puerto", type=int, default=8000,
                   help="puerto de la interfaz web (por defecto: 8000)")
    p.add_argument("--no-abrir", action="store_true",
                   help="con --web, no abrir el navegador automáticamente")
    p.add_argument("--idiomas", action="store_true",
                   help="mostrar los idiomas que admite Google y salir")
    p.add_argument("--crear-acceso-directo", action="store_true",
                   help="(Windows) crear el ícono «Texto a MP3» en el escritorio")
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
        if args.crear_acceso_directo:
            print(f"Ícono listo en el escritorio: {crear_acceso_directo()}")
            return 0

        if args.archivo and args.texto:
            parser.error("usa un texto o --archivo, pero no ambos a la vez")

        if args.web:
            iniciar_web(args.puerto, abrir_navegador=not args.no_abrir)
            return 0
        sin_texto = not (args.archivo or args.texto)
        if args.ventana or (sin_texto and (sys.stdin is None or sys.stdin.isatty())):
            iniciar_ventana()
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
