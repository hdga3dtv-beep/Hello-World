#!/usr/bin/env python3
"""Texto a MP3: convierte cualquier texto, o un PDF completo, en un archivo MP3.

Uso rápido:
    python texto_a_mp3.py                            # abre la ventana de la app
    python texto_a_mp3.py "Hola, mundo" -o hola.mp3
    python texto_a_mp3.py -a libro.pdf               # crea libro.mp3
    python texto_a_mp3.py --web                      # versión en el navegador

Motores de voz:
    offline  (por defecto) Voz natural de Piper que funciona sin internet.
             Cada voz se descarga una sola vez (unos 60 MB) y se guarda en la
             carpeta «voces». Necesita piper-tts y lameenc.
    google   Voz de Google. Necesita internet y la librería gTTS.

Para abrir PDF hace falta PyMuPDF. Todo se instala con:
    pip install -r requirements.txt
"""

import argparse
import contextlib
import difflib
import html
import io
import json
import os
import re
import subprocess
import sys
import threading
import time
import unicodedata
import urllib.error
import urllib.request
import webbrowser
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

CARPETA_APP = os.path.dirname(os.path.abspath(__file__))
CARPETA_VOCES = os.path.join(CARPETA_APP, "voces")

MOTORES = ("offline", "google")

# Idiomas del motor de Google que se muestran en la interfaz. Desde la línea
# de comandos se puede usar cualquier código que admita Google (ver --idiomas).
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

# Voces de Piper (motor sin internet): nombre que se muestra y tamaño en MB.
# Cada una se descarga una sola vez del catálogo oficial de Piper.
VOCES = {
    "es_MX-claude-high": ("Español (México) · Claude · la más natural", 60),
    "es_MX-ald-medium": ("Español (México) · Ald · más rápida", 60),
    "es_ES-davefx-medium": ("Español (España) · Davefx", 60),
    "es_AR-daniela-high": ("Español (Argentina) · Daniela", 109),
    "en_US-lessac-medium": ("Inglés (Estados Unidos) · Lessac", 60),
    "pt_BR-faber-medium": ("Portugués (Brasil) · Faber", 60),
    "fr_FR-siwis-medium": ("Francés · Siwis", 60),
    "it_IT-paola-medium": ("Italiano · Paola", 61),
    "de_DE-thorsten-medium": ("Alemán · Thorsten", 60),
    "ca_ES-upc_ona-medium": ("Catalán · Ona", 60),
}
VOZ_POR_IDIOMA = {
    "es": "es_MX-claude-high",
    "en": "en_US-lessac-medium",
    "pt": "pt_BR-faber-medium",
    "fr": "fr_FR-siwis-medium",
    "it": "it_IT-paola-medium",
    "de": "de_DE-thorsten-medium",
    "ca": "ca_ES-upc_ona-medium",
}
URL_VOCES = ("https://huggingface.co/rhasspy/piper-voices/resolve/main/"
             "{familia}/{codigo}/{nombre}/{calidad}/{voz}{extension}?download=true")

TROZO_MAXIMO = 500            # caracteres por trozo: el medidor avanza trozo a trozo
PAGINAS_SIN_PREGUNTAR = 20    # en PDF más largos, la ventana pregunta qué páginas leer
PAUSA_ORACION = 0.25          # segundos de silencio entre oraciones (voz sin internet)
PAUSA_PARRAFO = 0.6           # segundos de silencio entre párrafos
CARACTERES_POR_SEGUNDO = 14.5  # medido: así de rápido se oye el texto en español
KBPS_MP3 = 64                 # calidad del MP3: de sobra para voz (unos 29 MB por hora)
LIMITE_PETICION = 1_000_000   # bytes máximos aceptados por la interfaz web


class ErrorConversion(Exception):
    """Error con un mensaje pensado para mostrarse directamente al usuario."""


class Cancelado(ErrorConversion):
    """El usuario detuvo la conversión (o la lectura del PDF)."""

    def __init__(self, mensaje="Conversión detenida. No se guardó ningún archivo."):
        super().__init__(mensaje)


def _revisar_cancelacion(cancelar, mensaje=None):
    if cancelar is not None and cancelar.is_set():
        raise Cancelado(mensaje) if mensaje else Cancelado()


# --------------------------------------------------------------------------
# Conversión
# --------------------------------------------------------------------------

_PARRAFO = re.compile(r"\S[\s\S]*?(?=\n[ \t]*\n|\s*\Z)")
_CORTES = (
    re.compile(r"[.!?…]+[\"'»”’)\]]*\s+"),  # fin de oración
    re.compile(r"[,;:]\s+"),                # pausa dentro de una oración
    re.compile(r"\s+"),                     # entre dos palabras
)


def partir_texto(texto, maximo=TROZO_MAXIMO):
    """Divide ``texto`` en trozos de hasta ``maximo`` caracteres.

    Devuelve una lista de pares (inicio, fin) con la posición de cada trozo
    dentro de ``texto``, para poder marcar en la ventana lo que ya se
    convirtió. Corta entre párrafos y, si un párrafo es muy largo, al final de
    una oración (o, si no hay más remedio, entre comas o palabras).
    """
    trozos = []
    for parrafo in _PARRAFO.finditer(texto):
        inicio, fin = parrafo.span()
        while fin - inicio > maximo:
            corte = _mejor_corte(texto, inicio, inicio + maximo)
            trozos.append((inicio, inicio + len(texto[inicio:corte].rstrip())))
            inicio = corte
            while inicio < fin and texto[inicio].isspace():
                inicio += 1
        if inicio < fin:
            trozos.append((inicio, fin))
    return trozos


def _mejor_corte(texto, inicio, limite):
    for patron in _CORTES:
        cortes = [m.end() for m in patron.finditer(texto, inicio, limite)]
        if cortes:
            return cortes[-1]
    return limite  # una "palabra" larguísima: se corta tal cual


def voz_para(idioma):
    """Voz sin internet que se usa para un idioma (o la voz, si ya es una)."""
    if idioma in VOCES:
        return idioma
    voz = VOZ_POR_IDIOMA.get(idioma.lower().replace("_", "-").split("-")[0])
    if voz is None:
        raise ErrorConversion(
            f"No hay voz sin internet para {IDIOMAS.get(idioma, idioma)!r}. "
            "Usa el motor de Google.")
    return voz


def generar_mp3(texto, idioma="es", lento=False, motor="offline", voz=None,
                avance=None, cancelar=None):
    """Convierte ``texto`` en audio y devuelve los bytes del MP3."""
    archivo = io.BytesIO()
    _escribir_mp3(texto, archivo, idioma, lento, motor, voz, avance, cancelar)
    return archivo.getvalue()


def convertir(texto, salida, idioma="es", lento=False, motor="offline", voz=None,
              avance=None, cancelar=None):
    """Convierte ``texto`` y lo guarda en el archivo MP3 ``salida``.

    ``avance(fase, hechos, total, trozo)`` se llama mientras trabaja, para
    mostrar un medidor; ``cancelar`` es un ``threading.Event`` que detiene la
    conversión al terminar el trozo en curso.

    Devuelve la ruta absoluta del archivo creado. El MP3 se va escribiendo en
    «nombre.mp3.parcial» y solo se renombra al terminar bien, así nunca queda
    un MP3 a medias.
    """
    salida = os.path.abspath(salida)
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    parcial = salida + ".parcial"
    try:
        with open(parcial, "wb") as archivo:
            _escribir_mp3(texto, archivo, idioma, lento, motor, voz, avance, cancelar)
        try:
            os.replace(parcial, salida)
        except PermissionError:
            raise ErrorConversion(
                f"No se pudo guardar {os.path.basename(salida)!r}: ¿está abierto en "
                "otro programa? Ciérralo o elige otro nombre.") from None
    except BaseException:
        with contextlib.suppress(OSError):
            os.remove(parcial)
        raise
    return salida


def _escribir_mp3(texto, archivo, idioma, lento, motor, voz, avance, cancelar):
    """Convierte ``texto`` trozo a trozo y va escribiendo el MP3 en ``archivo``."""
    texto = texto or ""
    trozos = partir_texto(texto)
    if not trozos:
        raise ErrorConversion("No hay texto para convertir.")
    if motor not in MOTORES:
        raise ErrorConversion(
            f"Motor desconocido: {motor!r}. Usa uno de: {', '.join(MOTORES)}.")

    sintetizador = _crear_motor(motor, idioma, lento, voz, avance, cancelar)
    total = len(texto)
    for i, (inicio, fin) in enumerate(trozos):
        _revisar_cancelacion(cancelar)
        if avance:
            avance("convirtiendo", inicio, total, (inicio, fin))
        siguiente = trozos[i + 1][0] if i + 1 < len(trozos) else fin
        pausa = PAUSA_PARRAFO if texto.count("\n", fin, siguiente) >= 2 else PAUSA_ORACION
        archivo.write(sintetizador.trozo(" ".join(texto[inicio:fin].split()), pausa))
    archivo.write(sintetizador.terminar())
    if avance:
        avance("convirtiendo", total, total, None)


def _crear_motor(motor, idioma, lento, voz, avance, cancelar):
    if motor == "google":
        return _MotorGoogle(idioma, lento, cancelar)
    return _MotorPiper(voz or voz_para(idioma), lento, avance, cancelar)


class _MotorGoogle:
    """Convierte cada trozo con el servicio de voz de Google (con internet)."""

    REINTENTOS = 3

    def __init__(self, idioma, lento, cancelar=None):
        try:
            from gtts import gTTS
            from gtts.tts import gTTSError
        except ImportError:
            raise ErrorConversion(
                f"Falta la librería gTTS. Instálala con:  {_comando_pip('gTTS')}"
            ) from None
        self._gtts, self._error_gtts = gTTS, gTTSError
        self.idioma, self.lento, self.cancelar = idioma, lento, cancelar

    def trozo(self, texto, pausa=PAUSA_ORACION):
        for intento in range(1, self.REINTENTOS + 1):
            audio = io.BytesIO()
            try:
                self._gtts(texto, lang=self.idioma, slow=self.lento).write_to_fp(audio)
                return audio.getvalue()
            except ValueError as e:  # gTTS lanza ValueError si el idioma no existe
                raise ErrorConversion(
                    f"Google no admite el idioma {self.idioma!r}. "
                    "Usa --idiomas para ver la lista.") from e
            except self._error_gtts as e:
                if intento == self.REINTENTOS:
                    raise ErrorConversion(
                        "No se pudo conectar con el servicio de voz de Google. Revisa "
                        "tu conexión a internet o usa el motor sin internet. "
                        f"(Detalle: {e})") from e
                # Con textos largos Google a veces pide esperar un poco.
                if self.cancelar is not None:
                    self.cancelar.wait(3 * intento)
                else:
                    time.sleep(3 * intento)
                _revisar_cancelacion(self.cancelar)
        return b""

    def terminar(self):
        return b""


class _MotorPiper:
    """Convierte con una voz de Piper, sin internet, y codifica el MP3 al vuelo."""

    def __init__(self, voz, lento, avance=None, cancelar=None):
        try:
            import lameenc
            from piper import PiperVoice, SynthesisConfig
        except ImportError:
            raise ErrorConversion(
                "Para convertir sin internet faltan piper-tts y lameenc. "
                f"Instálalos con:  {_comando_pip('piper-tts lameenc')}") from None
        modelo = asegurar_voz(voz, avance, cancelar)
        if avance:
            avance("preparando", 0, 0, None)
        try:
            self.voz = PiperVoice.load(modelo)
        except Exception as e:
            raise ErrorConversion(
                f"No se pudo cargar la voz {voz!r} ({e}). Borra sus archivos de la "
                "carpeta «voces» para que se descargue de nuevo.") from e
        self.tasa = self.voz.config.sample_rate
        self.config = SynthesisConfig(length_scale=1.3 if lento else None)
        self.mp3 = lameenc.Encoder()
        self.mp3.set_bit_rate(KBPS_MP3)
        self.mp3.set_in_sample_rate(self.tasa)
        self.mp3.set_channels(1)
        self.mp3.set_quality(2)

    def _silencio(self, segundos):
        return bytes(2 * int(self.tasa * segundos))  # muestras de 16 bits en cero

    def trozo(self, texto, pausa=PAUSA_ORACION):
        partes = []
        for i, audio in enumerate(self.voz.synthesize(texto, self.config)):
            if i:  # Piper entrega una oración a la vez
                partes.append(self._silencio(PAUSA_ORACION))
            partes.append(audio.audio_int16_bytes)
        partes.append(self._silencio(pausa))
        return bytes(self.mp3.encode(b"".join(partes)))

    def terminar(self):
        return bytes(self.mp3.flush())


def ruta_voz(voz):
    return os.path.join(CARPETA_VOCES, voz + ".onnx")


def voz_descargada(voz):
    modelo = ruta_voz(voz)
    return all(os.path.isfile(r) and os.path.getsize(r) > 0
               for r in (modelo, modelo + ".json"))


def asegurar_voz(voz, avance=None, cancelar=None):
    """Devuelve la ruta del modelo de la voz, descargándola si hace falta."""
    if voz not in VOCES:
        raise ErrorConversion(f"Voz desconocida: {voz!r}. Usa --voces para ver la lista.")
    if not voz_descargada(voz):
        descargar_voz(voz, avance, cancelar)
    return ruta_voz(voz)


def descargar_voz(voz, avance=None, cancelar=None):
    """Descarga la voz (modelo .onnx y su .onnx.json) a la carpeta «voces».

    Cada archivo se baja primero a «.descargando» y se renombra al terminar,
    así una descarga cortada nunca deja una voz rota.
    """
    familia, resto = voz.split("_", 1)
    region, nombre, calidad = resto.split("-", 2)
    os.makedirs(CARPETA_VOCES, exist_ok=True)
    modelo = ruta_voz(voz)
    for extension, destino in ((".onnx.json", modelo + ".json"), (".onnx", modelo)):
        url = URL_VOCES.format(familia=familia, codigo=f"{familia}_{region}",
                               nombre=nombre, calidad=calidad, voz=voz,
                               extension=extension)
        temporal = destino + ".descargando"
        try:
            with urllib.request.urlopen(url, timeout=60) as respuesta, \
                    open(temporal, "wb") as f:
                total = int(respuesta.headers.get("Content-Length") or 0)
                hechos = 0
                while True:
                    _revisar_cancelacion(cancelar, "Descarga de la voz detenida.")
                    bloque = respuesta.read(256 * 1024)
                    if not bloque:
                        break
                    f.write(bloque)
                    hechos += len(bloque)
                    if avance and extension == ".onnx":
                        avance("descargando", hechos, total, None)
            os.replace(temporal, destino)
        except OSError as e:  # incluye los errores de red (URLError)
            raise ErrorConversion(
                "No se pudo descargar la voz. La primera vez hace falta internet; "
                f"después ya convierte sin conexión. (Detalle: {e})") from e
        finally:
            with contextlib.suppress(OSError):
                os.remove(temporal)


def _comando_pip(paquete):
    """Comando para instalar ``paquete`` en el Python que ejecuta la app."""
    if sys.prefix != sys.base_prefix:  # entorno propio (p. ej. el del lanzador)
        return f'"{sys.executable}" -m pip install {paquete}'
    return f"pip install {paquete}"


# --------------------------------------------------------------------------
# Lectura de archivos (.txt y .pdf)
# --------------------------------------------------------------------------

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


def leer_documento(ruta, avance=None, cancelar=None, desde=1, hasta=None):
    """Lee el texto de un .pdf (solo de ``desde`` a ``hasta``) o de un archivo de texto."""
    if ruta.lower().endswith(".pdf"):
        return leer_pdf(ruta, avance, cancelar, desde, hasta)
    return leer_archivo(ruta)


# Números de página: «23», «- 23 -» o romanos en minúscula («xiv»). Los romanos
# en mayúscula no, porque suelen ser títulos de capítulo («II»).
_SOLO_NUMERO = re.compile(r"[\s\-–—.|]*(\d{1,4}|[ivxlcdm]{1,8})[\s\-–—.|]*")
_LLAMADA_NOTA = re.compile(r"[\s\d*†‡§¹²³⁰-⁹,]+")
_FIN_DE_FRASE = ".!?…:»”\"')]"
_LIGADURAS = str.maketrans({"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl",
                            "ﬅ": "st", "ﬆ": "st", "\xad": ""})
_VINETAS = re.compile(r"[•▪●■◦►✓❖➢]\s*")


def _abrir_pdf(ruta):
    try:
        import pymupdf
    except ImportError:
        raise ErrorConversion(
            f"Para abrir PDF falta PyMuPDF. Instálalo con:  {_comando_pip('pymupdf')}"
        ) from None
    try:
        documento = pymupdf.open(ruta)
    except Exception as e:
        raise ErrorConversion(f"No se pudo abrir el PDF {os.path.basename(ruta)!r}: {e}") from e
    if documento.needs_pass:
        documento.close()
        raise ErrorConversion("El PDF está protegido con contraseña.")
    return documento


def contar_paginas(ruta):
    with _abrir_pdf(ruta) as documento:
        return documento.page_count


def leer_pdf(ruta, avance=None, cancelar=None, desde=1, hasta=None):
    """Extrae el texto de un PDF (de la página ``desde`` a ``hasta``) para leerlo en voz alta.

    Quita lo que estorba al escuchar: números de página, encabezados y pies que
    se repiten en las páginas, notas al pie y sus llamadas (¹, ², *). Une las
    palabras partidas con guion al final de la línea y los párrafos que siguen
    en la página siguiente.
    """
    import pymupdf

    with _abrir_pdf(ruta) as documento:
        total = documento.page_count
        ultima = total if hasta is None else min(hasta, total)
        primera = max(1, desde)
        if primera > ultima:
            raise ErrorConversion(f"El PDF tiene {total} páginas; "
                                  "elige páginas dentro de ese rango.")
        # Se leen también hasta 10 páginas vecinas, solo para comparar: así se
        # reconocen la letra del cuerpo y los encabezados aunque elijas una sola página.
        contexto = range(max(1, primera - 10), min(total, ultima + 10) + 1)
        # Sin las imágenes: en un libro escaneado, leerlas hace todo 50 veces más lento.
        opciones = pymupdf.TEXTFLAGS_DICT & ~pymupdf.TEXT_PRESERVE_IMAGES
        paginas = []
        for leidas, numero in enumerate(contexto, 1):
            _revisar_cancelacion(cancelar, "Lectura del PDF detenida.")
            paginas.append(_bloques_de_pagina(documento[numero - 1], opciones))
            if avance:
                avance("leyendo", leidas, len(contexto), None)

    elegidas = range(primera - contexto.start, ultima - contexto.start + 1)
    texto = _armar_texto(paginas, elegidas)
    if not texto.strip():
        raise ErrorConversion(
            "No encontré texto en este PDF. Si es un escaneo (fotos de las páginas), "
            "primero hay que pasarlo por un programa de reconocimiento de texto (OCR).")
    return texto


def _bloques_de_pagina(pagina, opciones):
    """Bloques de texto de una página: posición y, por línea, (texto, tamaño, flags)."""
    bloques = []
    for bloque in pagina.get_text("dict", flags=opciones)["blocks"]:
        if bloque.get("type") != 0:  # 1 = imagen
            continue
        lineas = []
        for linea in bloque["lines"]:
            if abs(linea.get("dir", (1, 0))[1]) > 0.1:  # texto girado en el margen
                continue
            spans = [(s["text"], round(s["size"] * 2) / 2, s["flags"]) for s in linea["spans"]]
            if any(t.strip() for t, _, _ in spans):
                lineas.append(spans)
        if lineas:
            bloques.append({"y0": bloque["bbox"][1], "y1": bloque["bbox"][3],
                            "lineas": lineas})
    return bloques


def _tamano_principal(paginas):
    """Tamaño de letra del cuerpo del texto: el que más caracteres tiene."""
    conteo = Counter()
    for bloques in paginas:
        for bloque in bloques:
            for linea in bloque["lineas"]:
                for texto, tamano, _ in linea:
                    conteo[tamano] += len(texto.strip())
    return conteo.most_common(1)[0][0] if conteo else 0


def _tamano_bloque(bloque):
    conteo = Counter()
    for linea in bloque["lineas"]:
        for texto, tamano, _ in linea:
            conteo[tamano] += len(texto.strip())
    return conteo.most_common(1)[0][0]


def _texto_linea(spans, principal):
    """Texto de una línea sin las llamadas a nota (superíndices como ¹ o *)."""
    partes = []
    for texto, tamano, flags in spans:
        llamada = flags & 1 or tamano < principal * 0.75  # superíndice o letra muy chica
        if llamada and texto.strip() and _LLAMADA_NOTA.fullmatch(texto):
            continue
        partes.append(texto)
    return " ".join("".join(partes).split())


def _texto_bloque(bloque, principal):
    texto = ""
    for linea in bloque["lineas"]:
        parte = _texto_linea(linea, principal)
        if parte:
            texto = _unir(texto, parte) if texto else parte
    return texto


def _quitar_notas_al_pie(bloques, principal):
    """Quita los bloques en letra más chica que quedan debajo del cuerpo del texto."""
    cuerpo = [b for b in bloques if _tamano_bloque(b) >= principal * 0.9
              and sum(len(t) for linea in b["lineas"] for t, _, _ in linea) > 15]
    if not cuerpo:
        return bloques  # página toda en letra chica: no hay con qué comparar
    limite = max(b["y1"] for b in cuerpo)
    return [b for b in bloques
            if not (b["y0"] >= limite - 1 and _tamano_bloque(b) < principal * 0.9)]


def _orillas(textos):
    """Índices de los dos bloques de más arriba y los dos de más abajo."""
    por_arriba = sorted(range(len(textos)), key=lambda i: textos[i][0]["y0"])
    por_abajo = sorted(range(len(textos)), key=lambda i: -textos[i][0]["y1"])
    return set(por_arriba[:2]) | set(por_abajo[:2])


def _clave(texto):
    """Texto simplificado para comparar encabezados: sin tildes, signos ni números."""
    sin_tildes = unicodedata.normalize("NFD", texto.lower()).encode("ascii", "ignore").decode()
    return " ".join(re.sub(r"\d+", "#", re.sub(r"[^a-z\d]+", " ", sin_tildes)).split())


def _parecidas(a, b):
    """¿Dos claves son el mismo encabezado, aunque el OCR cambie alguna letra?"""
    if a == b:
        return True
    if abs(len(a) - len(b)) > 0.3 * max(len(a), len(b)):
        return False
    comparador = difflib.SequenceMatcher(None, a, b)
    return comparador.real_quick_ratio() >= 0.8 and comparador.ratio() >= 0.8


def _parece_basura(texto):
    """Renglón de OCR revuelto, como «( apitii i o o t h . - s a r»."""
    sin_espacios = texto.replace(" ", "")
    palabras = texto.split()
    sueltas = sum(1 for p in palabras if len(p) == 1)
    letras = sum(c.isalpha() for c in sin_espacios)
    return ((len(sin_espacios) >= 8 and letras < 0.5 * len(sin_espacios))  # «—No.» no es basura
            or (len(palabras) >= 4 and sueltas >= 0.4 * len(palabras)))


def _continua(anterior, siguiente):
    """¿``siguiente`` sigue el mismo párrafo (cortado por un salto de página)?"""
    if re.search(r"[^\W\d_][-\xad‐]$", anterior):
        return True
    return not anterior.endswith(tuple(_FIN_DE_FRASE)) and siguiente[:1].islower()


def _unir(anterior, siguiente):
    """Une dos pedazos de texto, pegando las palabras partidas con guion."""
    if re.search(r"[^\W\d_][-\xad‐]$", anterior) and siguiente[:1].islower():
        return anterior[:-1] + siguiente
    return anterior + " " + siguiente


def _armar_texto(paginas, elegidas=None):
    """Texto limpio de las páginas ``elegidas`` (índices); las demás solo se comparan."""
    principal = _tamano_principal(paginas)
    por_pagina = []
    for bloques in paginas:
        bloques = _quitar_notas_al_pie(bloques, principal)
        textos = [(b, t) for b in bloques if (t := _texto_bloque(b, principal))]
        por_pagina.append(textos)

    encabezados = _encabezados_y_pies(por_pagina)
    parrafos = []
    for indice in elegidas if elegidas is not None else range(len(por_pagina)):
        textos = por_pagina[indice]
        orillas = _orillas(textos)
        for i, (_, texto) in enumerate(textos):
            if (indice, i) in encabezados:
                continue
            if i in orillas and len(texto) <= 120 and (
                    _SOLO_NUMERO.fullmatch(texto) or _parece_basura(texto)):
                continue
            if parrafos and _continua(parrafos[-1], texto):
                parrafos[-1] = _unir(parrafos[-1], texto)
            else:
                parrafos.append(texto)
    return _VINETAS.sub("", "\n\n".join(parrafos).translate(_LIGADURAS))


def _encabezados_y_pies(por_pagina, vecindad=4):
    """(página, bloque) de los encabezados y pies de página.

    Son textos cortos en la orilla de la página que se repiten, iguales o
    parecidos, en al menos otras dos páginas cercanas (a 4 páginas o menos).
    Los números se ignoran: «Capítulo 2 · 45» = «Capítulo 2 · 46». Pedir dos
    páginas cercanas evita borrar una línea corta de diálogo («—No.») que cayó
    arriba de una página por casualidad.
    """
    orillas = {}
    for numero, textos in enumerate(por_pagina):
        orillas[numero] = [(i, _clave(textos[i][1])) for i in _orillas(textos)
                           if len(textos[i][1]) <= 120]
    encontrados = set()
    for numero, candidatos in orillas.items():
        for i, clave in candidatos:
            if not clave:
                continue
            vecinas = {otra for otra in range(numero - vecindad, numero + vecindad + 1)
                       if otra != numero
                       and any(_parecidas(clave, c) for _, c in orillas.get(otra, ()))}
            if len(vecinas) >= 2:
                encontrados.add((numero, i))
    return encontrados


# --------------------------------------------------------------------------
# Formatos para mostrar
# --------------------------------------------------------------------------

def _miles(numero):
    """12345 -> '12 345'."""
    return f"{numero:,}".replace(",", " ")


def _duracion(segundos):
    """'menos de 1 min', '12 min' o '1 h 05 min'."""
    minutos = round(segundos / 60)
    if minutos < 1:
        return "menos de 1 min"
    if minutos < 60:
        return f"{minutos} min"
    return f"{minutos // 60} h {minutos % 60:02d} min"


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
          <option value="offline">Sin internet (voz natural)</option>
          <option value="google">Google (con internet)</option>
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
  La primera vez que uses una voz sin internet, se descarga (unos 60 MB).
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
                motor=str(datos.get("motor") or "offline"),
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

ICONO = os.path.join(CARPETA_APP, "icono.ico")
NOMBRES_MOTOR = {"offline": "Sin internet (voz natural)", "google": "Google (con internet)"}
NOMBRES_VOZ = {voz: nombre for voz, (nombre, _) in VOCES.items()}
_COLOR_SUAVE, _COLOR_ERROR, _COLOR_EXITO = "#5b6475", "#b3261e", "#1e7b34"
_COLOR_BOTON, _COLOR_BOTON_HOVER = "#2f6fed", "#2459c4"
_COLOR_DETENER, _COLOR_DETENER_HOVER = "#b3261e", "#8c1d18"
_FONDO_CONVERTIDO, _FONDO_ACTUAL = "#dcefe0", "#fff0b3"


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
        self._nombre_desde_archivo = None
        self._eleccion = {"offline": VOZ_POR_IDIOMA["es"], "google": "es"}
        self._cancelar = threading.Event()
        self._resultado = None
        self._al_terminar = None
        self._avance = None
        self._avance_pintado = None
        self._inicio_conversion = None
        self._visto_hasta = None
        self._ocupada = False

        raiz.title("Texto a MP3")
        escala = raiz.winfo_fpixels("1i") / 96  # pantallas con zoom (125 %, 150 %...)
        raiz.geometry(f"{int(760 * escala)}x{int(680 * escala)}")
        raiz.minsize(int(620 * escala), int(520 * escala))
        if sys.platform == "win32" and os.path.exists(ICONO):
            try:
                raiz.iconbitmap(default=ICONO)
            except tk.TclError:
                pass
        raiz.report_callback_exception = self._error_inesperado
        raiz.protocol("WM_DELETE_WINDOW", self._al_cerrar)

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
        ttk.Label(cabecera, text="Escribe o pega el texto, o abre un archivo .txt o un PDF:",
                  foreground=_COLOR_SUAVE).pack(side="left")
        self.boton_abrir = ttk.Button(cabecera, text="Abrir .txt o PDF…",
                                      command=self.abrir_archivo)
        self.boton_abrir.pack(side="right")

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
        # Lo ya convertido se pinta de verde; el trozo que se está convirtiendo, de amarillo.
        self.texto.tag_configure("convertido", background=_FONDO_CONVERTIDO)
        self.texto.tag_configure("actual", background=_FONDO_ACTUAL)
        self.texto.tag_raise("actual")

        self.contador = ttk.Label(marco, text="0 caracteres", foreground=_COLOR_SUAVE)
        self.contador.grid(row=3, column=0, sticky="e", pady=(4, 0))

        opciones = ttk.Frame(marco)
        opciones.grid(row=4, column=0, sticky="ew", pady=(6, 14))
        ttk.Label(opciones, text="Motor de voz").grid(row=0, column=0, sticky="w")
        self.etiqueta_voz = ttk.Label(opciones, text="Voz")
        self.etiqueta_voz.grid(row=0, column=1, sticky="w", padx=(16, 0))
        self.motor = ttk.Combobox(opciones, state="readonly", width=24,
                                  values=list(NOMBRES_MOTOR.values()), font=(familia, 10))
        self.motor.current(0)
        self.motor.grid(row=1, column=0, sticky="w", pady=(3, 0))
        self.motor.bind("<<ComboboxSelected>>", lambda e: self._actualizar_voces())
        self.voz = ttk.Combobox(opciones, state="readonly", width=40, font=(familia, 10))
        self.voz.grid(row=1, column=1, sticky="w", padx=(16, 0), pady=(3, 0))
        self.voz.bind("<<ComboboxSelected>>", self._al_elegir_voz)
        self.lento = tk.BooleanVar(value=False)
        ttk.Checkbutton(opciones, text="Leer más despacio", variable=self.lento).grid(
            row=1, column=2, sticky="w", padx=(20, 0), pady=(3, 0))
        self.aviso_voz = ttk.Label(opciones, foreground=_COLOR_SUAVE)
        self.aviso_voz.grid(row=2, column=0, columnspan=3, sticky="w", pady=(6, 0))

        botones = ttk.Frame(marco)
        botones.grid(row=5, column=0, sticky="ew")
        botones.columnconfigure(0, weight=1)
        self.boton = tk.Button(
            botones, text="Convertir y guardar MP3…", command=self.convertir_y_guardar,
            font=(familia, 12, "bold"), bg=_COLOR_BOTON, fg="white",
            activebackground=_COLOR_BOTON_HOVER, activeforeground="white",
            disabledforeground="#dfe7ff", relief="flat", borderwidth=0,
            cursor="hand2", padx=12, pady=9)
        self.boton.grid(row=0, column=0, sticky="ew")
        self.boton_escuchar = ttk.Button(botones, text="▶  Escuchar",
                                         command=self.escuchar, state="disabled")
        self.boton_escuchar.grid(row=0, column=1, sticky="ns", padx=(10, 0))
        self.boton_carpeta = ttk.Button(botones, text="Abrir carpeta",
                                        command=self.abrir_carpeta, state="disabled")
        self.boton_carpeta.grid(row=0, column=2, sticky="ns", padx=(8, 0))

        self.progreso = ttk.Progressbar(marco, mode="determinate", maximum=100)
        self.progreso.grid(row=6, column=0, sticky="ew", pady=(14, 0))
        self.progreso.grid_remove()
        self.detalle = ttk.Label(marco, font=(familia, 10, "bold"))
        self.detalle.grid(row=7, column=0, sticky="w", pady=(6, 0))
        self.detalle.grid_remove()
        self.estado = ttk.Label(marco, justify="left")
        self.estado.grid(row=8, column=0, sticky="ew", pady=(10, 0))
        marco.bind("<Configure>",
                   lambda e: self.estado.configure(wraplength=max(200, e.width - 48)))
        self._mostrar_estado("Atajo: Ctrl + Enter para convertir.")

        self.texto.bind("<<Modified>>", self._al_modificar)
        self.texto.bind("<Control-a>", self._seleccionar_todo)
        self.texto.bind("<Control-Return>", self._atajo_convertir)
        raiz.bind("<Control-Return>", self._atajo_convertir)
        self._actualizar_voces()
        self.texto.focus_set()

    # --- acciones -------------------------------------------------------

    def abrir_archivo(self):
        from tkinter import filedialog

        if self._ocupada:
            return
        ruta = filedialog.askopenfilename(
            parent=self.raiz, title="Abrir texto o PDF",
            filetypes=[("Texto o PDF", "*.txt *.pdf"), ("PDF", "*.pdf"),
                       ("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if not ruta:
            return
        rango = None
        if ruta.lower().endswith(".pdf"):
            try:
                total = contar_paginas(ruta)
            except ErrorConversion as e:
                self._mostrar_estado(str(e), color=_COLOR_ERROR)
                return
            desde, hasta = 1, total
            if total > PAGINAS_SIN_PREGUNTAR:  # un libro: mejor elegir el capítulo
                elegido = self._pedir_paginas(os.path.basename(ruta), total)
                if elegido is None:
                    return
                desde, hasta = elegido
            rango = (desde, hasta, total)
        self._iniciar(
            lambda avance, cancelar: leer_documento(ruta, avance, cancelar,
                                                    *(rango[:2] if rango else ())),
            lambda tipo, valor: self._fin_lectura(tipo, valor, ruta, rango))

    def convertir_y_guardar(self):
        from tkinter import filedialog

        if self._ocupada:  # durante el trabajo, el botón sirve para detener
            self.detener()
            return
        texto = self.texto.get("1.0", "end-1c")
        if not texto.strip():
            self._mostrar_estado("Escribe algún texto primero.", color=_COLOR_ERROR)
            self.texto.focus_set()
            return
        ruta = filedialog.asksaveasfilename(
            parent=self.raiz, title="Guardar el audio como",
            defaultextension=".mp3", filetypes=[("Audio MP3", "*.mp3")],
            initialdir=self.carpeta_guardado,
            initialfile=self._nombre_desde_archivo or nombre_sugerido(texto))
        if not ruta:
            return
        if not ruta.lower().endswith(".mp3"):
            ruta += ".mp3"
        self.carpeta_guardado = os.path.dirname(ruta)
        motor = self._motor_elegido()
        opciones = {"motor": motor, "lento": self.lento.get()}
        if motor == "google":
            opciones["idioma"] = self._eleccion["google"]
        else:
            opciones["voz"] = self._eleccion["offline"]

        self._limpiar_marcas()
        self.texto.configure(state="disabled")  # que no cambie mientras se convierte
        self._iniciar(
            lambda avance, cancelar: convertir(texto, ruta, avance=avance,
                                               cancelar=cancelar, **opciones),
            self._fin_conversion)

    def detener(self):
        self._cancelar.set()
        self.boton.configure(text="Deteniendo…", state="disabled")
        self._mostrar_estado("Deteniendo… espera a que termine el trozo en curso.")

    def escuchar(self):
        self._abrir(self.ultimo_mp3)

    def abrir_carpeta(self):
        self._abrir(self.ultimo_mp3, mostrar_en_carpeta=True)

    # --- trabajo en segundo plano -----------------------------------------

    def _iniciar(self, tarea, al_terminar):
        """Ejecuta ``tarea(avance, cancelar)`` en otro hilo, sin congelar la ventana."""
        self._cancelar = threading.Event()
        self._resultado = None
        self._avance = self._avance_pintado = None
        self._inicio_conversion = None
        self._al_terminar = al_terminar
        self._ocupar(True)

        def trabajar():
            try:
                self._resultado = ("ok", tarea(self._al_avanzar, self._cancelar))
            except Cancelado as e:
                self._resultado = ("cancelado", str(e))
            except ErrorConversion as e:
                self._resultado = ("error", str(e))
            except Exception as e:
                self._resultado = ("error", f"Error inesperado: {e}")

        threading.Thread(target=trabajar, daemon=True).start()
        self.raiz.after(150, self._revisar)

    def _al_avanzar(self, fase, hechos=0, total=0, trozo=None):
        # Se llama desde el otro hilo: solo se guarda; la ventana lo pinta en _revisar.
        self._avance = (fase, hechos, total, trozo)

    def _revisar(self):
        avance = self._avance
        if avance is not None and avance != self._avance_pintado:
            self._avance_pintado = avance
            self._pintar_avance(*avance)
        if self._resultado is None:
            self.raiz.after(150, self._revisar)
            return
        tipo, valor = self._resultado
        self._ocupar(False)
        self._al_terminar(tipo, valor)

    def _pintar_avance(self, fase, hechos, total, trozo):
        if fase == "preparando":
            if str(self.progreso.cget("mode")) != "indeterminate":
                self.progreso.configure(mode="indeterminate")
                self.progreso.start(12)
            self.detalle.configure(text="Preparando la voz…")
            return
        if str(self.progreso.cget("mode")) == "indeterminate":
            self.progreso.stop()
            self.progreso.configure(mode="determinate")
        porcentaje = 100 * hechos / total if total else 0
        self.progreso.configure(value=porcentaje)
        if fase == "descargando":
            mb = 1024 * 1024
            self.detalle.configure(
                text=f"Descargando la voz (solo esta vez): {hechos / mb:.0f} de {total / mb:.0f} MB")
        elif fase == "leyendo":
            self.detalle.configure(text=f"Leyendo el PDF: {porcentaje:.0f} %")
        else:
            if self._inicio_conversion is None:
                self._inicio_conversion = (time.monotonic(), hechos)
            mensaje = (f"Convertido: {porcentaje:.0f} %  ({_miles(hechos)} de "
                       f"{_miles(total)} caracteres)")
            inicio, hechos_al_inicio = self._inicio_conversion
            transcurrido = time.monotonic() - inicio
            if hechos > hechos_al_inicio and transcurrido > 5:
                velocidad = (hechos - hechos_al_inicio) / transcurrido
                mensaje += f"  ·  tiempo restante: {_duracion((total - hechos) / velocidad)}"
            self.detalle.configure(text=mensaje)
            self._marcar(hechos, trozo)

    def _fin_lectura(self, tipo, valor, ruta, rango=None):
        if tipo != "ok":
            self._mostrar_estado(valor, color=_COLOR_ERROR if tipo == "error" else _COLOR_SUAVE)
            return
        self.texto.delete("1.0", "end")
        self.texto.insert("1.0", valor)
        self.texto.mark_set("insert", "1.0")
        self.texto.see("1.0")
        nombre = os.path.basename(ruta)
        base = os.path.splitext(nombre)[0]
        mensaje = f"Texto cargado de «{nombre}»"
        if rango:
            desde, hasta, total = rango
            if (desde, hasta) == (1, total):
                mensaje += f" ({total} páginas)"
            else:
                base += f" (págs. {desde}-{hasta})"
                mensaje += f" (páginas {desde} a {hasta} de {total})"
            mensaje += ". Se quitaron números de página, encabezados y notas al pie"
        self._nombre_desde_archivo = base + ".mp3"
        self._mostrar_estado(mensaje + ". Revísalo y pulsa Convertir.")

    def _pedir_paginas(self, nombre, total):
        """Pregunta qué páginas del PDF leer. Devuelve (desde, hasta) o None."""
        import tkinter as tk
        from tkinter import font as tkfont
        from tkinter import ttk

        familia = tkfont.nametofont("TkDefaultFont").actual("family")
        dialogo = tk.Toplevel(self.raiz)
        dialogo.title("Páginas del PDF")
        dialogo.transient(self.raiz)
        dialogo.resizable(False, False)
        dialogo.geometry(f"+{self.raiz.winfo_rootx() + 80}+{self.raiz.winfo_rooty() + 120}")
        marco = ttk.Frame(dialogo, padding=20)
        marco.pack(fill="both", expand=True)
        ttk.Label(marco, text=f"«{nombre}» tiene {total} páginas.",
                  font=(familia, 11, "bold"), wraplength=420).grid(
            row=0, column=0, columnspan=4, sticky="w")
        ttk.Label(marco, foreground=_COLOR_SUAVE, wraplength=420, justify="left",
                  text="¿Cuáles quieres convertir? Usa los números que muestra tu lector "
                       "de PDF (a veces no coinciden con los impresos en el libro).").grid(
            row=1, column=0, columnspan=4, sticky="w", pady=(4, 12))
        desde, hasta = tk.StringVar(value="1"), tk.StringVar(value=str(total))
        ttk.Label(marco, text="De la página").grid(row=2, column=0, sticky="w")
        primera = ttk.Spinbox(marco, from_=1, to=total, textvariable=desde, width=7)
        primera.grid(row=2, column=1, padx=6)
        ttk.Label(marco, text="a la").grid(row=2, column=2)
        ttk.Spinbox(marco, from_=1, to=total, textvariable=hasta, width=7).grid(
            row=2, column=3, padx=6, sticky="w")
        aviso = ttk.Label(marco, foreground=_COLOR_ERROR)
        aviso.grid(row=3, column=0, columnspan=4, sticky="w", pady=(6, 0))
        respuesta = []

        def aceptar(_evento=None):
            try:
                a, b = int(desde.get()), int(hasta.get())
            except ValueError:
                aviso.configure(text="Escribe dos números de página.")
                return
            a, b = sorted((min(max(a, 1), total), min(max(b, 1), total)))
            respuesta.append((a, b))
            dialogo.destroy()

        def todo():
            desde.set("1")
            hasta.set(str(total))
            aceptar()

        botones = ttk.Frame(marco)
        botones.grid(row=4, column=0, columnspan=4, sticky="e", pady=(14, 0))
        ttk.Button(botones, text="Cancelar", command=dialogo.destroy).pack(side="left")
        ttk.Button(botones, text="Todo el PDF", command=todo).pack(side="left", padx=8)
        ttk.Button(botones, text="Abrir estas páginas", command=aceptar).pack(side="left")
        dialogo.bind("<Return>", aceptar)
        dialogo.bind("<Escape>", lambda e: dialogo.destroy())
        primera.focus_set()
        primera.selection_range(0, "end")
        dialogo.grab_set()
        dialogo.wait_window()
        return respuesta[0] if respuesta else None

    def _fin_conversion(self, tipo, valor):
        self.texto.configure(state="normal")
        self._actualizar_aviso_voz()  # la voz pudo haberse descargado
        if tipo == "ok":
            self.ultimo_mp3 = valor
            self.boton_escuchar.configure(state="normal")
            self.boton_carpeta.configure(state="normal")
            self._marcar(len(self.texto.get("1.0", "end-1c")))
            self._mostrar_estado(f"✔  Listo. Guardado en: {valor}", color=_COLOR_EXITO)
        else:
            self._limpiar_marcas()
            self._mostrar_estado(valor, color=_COLOR_ERROR if tipo == "error" else _COLOR_SUAVE)

    def _ocupar(self, ocupada):
        self._ocupada = ocupada
        estado = "disabled" if ocupada else "normal"
        self.boton_abrir.configure(state=estado)
        self.motor.configure(state="disabled" if ocupada else "readonly")
        self.voz.configure(state="disabled" if ocupada else "readonly")
        if ocupada:
            self.boton.configure(text="■  Detener", state="normal", bg=_COLOR_DETENER,
                                 activebackground=_COLOR_DETENER_HOVER)
            self.progreso.configure(mode="indeterminate", value=0)
            self.progreso.grid()
            self.progreso.start(12)
            self.detalle.configure(text="Empezando…")
            self.detalle.grid()
            self._mostrar_estado("Puedes detenerlo cuando quieras con el botón rojo.")
        else:
            self.boton.configure(text="Convertir y guardar MP3…", state="normal",
                                 bg=_COLOR_BOTON, activebackground=_COLOR_BOTON_HOVER)
            self.progreso.stop()
            self.progreso.grid_remove()
            self.detalle.grid_remove()

    # --- detalles internos ----------------------------------------------

    def _motor_elegido(self):
        return self._codigo(self.motor.get(), NOMBRES_MOTOR, "offline")

    def _actualizar_voces(self):
        """El segundo menú muestra voces (sin internet) o idiomas (Google)."""
        if self._motor_elegido() == "google":
            self.etiqueta_voz.configure(text="Idioma")
            self.voz.configure(values=list(IDIOMAS.values()))
            self.voz.set(IDIOMAS[self._eleccion["google"]])
        else:
            self.etiqueta_voz.configure(text="Voz")
            self.voz.configure(values=list(NOMBRES_VOZ.values()))
            self.voz.set(NOMBRES_VOZ[self._eleccion["offline"]])
        self._actualizar_aviso_voz()

    def _al_elegir_voz(self, _evento=None):
        motor = self._motor_elegido()
        tabla = IDIOMAS if motor == "google" else NOMBRES_VOZ
        self._eleccion[motor] = self._codigo(self.voz.get(), tabla, self._eleccion[motor])
        self._actualizar_aviso_voz()

    def _actualizar_aviso_voz(self):
        if self._motor_elegido() == "google":
            aviso = "Usa la voz de Google: necesita internet mientras convierte."
        else:
            voz = self._eleccion["offline"]
            if voz_descargada(voz):
                aviso = "✔ Voz descargada: convierte sin internet."
            else:
                aviso = (f"Esta voz se descarga una sola vez ({VOCES[voz][1]} MB); "
                         "después convierte sin internet.")
        self.aviso_voz.configure(text=aviso)

    def _marcar(self, hechos, trozo=None):
        """Pinta de verde lo ya convertido y de amarillo el trozo en curso."""
        self.texto.tag_remove("actual", "1.0", "end")
        self.texto.tag_add("convertido", "1.0", f"1.0 + {hechos} chars")
        if trozo:
            inicio, fin = trozo
            self.texto.tag_add("actual", f"1.0 + {inicio} chars", f"1.0 + {fin} chars")
            # Sigue la lectura, salvo que te hayas ido a leer otra parte del texto
            # (el final del trozo anterior, que se dejó a la vista, ya no se ve).
            anterior = self._visto_hasta
            if anterior is None or self.texto.bbox(f"1.0 + {anterior} chars") is not None:
                self.texto.see(f"1.0 + {fin} chars")
                self._visto_hasta = fin

    def _limpiar_marcas(self):
        self._visto_hasta = None
        self.texto.tag_remove("convertido", "1.0", "end")
        self.texto.tag_remove("actual", "1.0", "end")

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
        mensaje = f"{n} carácter" if n == 1 else f"{_miles(n)} caracteres"
        if n / CARACTERES_POR_SEGUNDO >= 60:
            mensaje += f"  ·  ≈ {_duracion(n / CARACTERES_POR_SEGUNDO)} de audio"
        self.contador.configure(text=mensaje)
        if not self._ocupada:
            self._limpiar_marcas()  # el texto cambió: las marcas ya no valen
        self.texto.edit_modified(False)

    def _seleccionar_todo(self, _evento=None):
        self.texto.tag_add("sel", "1.0", "end-1c")
        return "break"

    def _atajo_convertir(self, _evento=None):
        if not self._ocupada:  # el atajo nunca detiene por accidente
            self.convertir_y_guardar()
        return "break"

    def _al_cerrar(self):
        from tkinter import messagebox

        if self._ocupada and not messagebox.askyesno(
                "Texto a MP3", "Todavía está convirtiendo. ¿Detener y cerrar?",
                parent=self.raiz):
            return
        self._cancelar.set()
        self.raiz.destroy()

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
  python texto_a_mp3.py -a libro.pdf                  (crea libro.mp3, sin internet)
  python texto_a_mp3.py -a cuento.txt -v es_MX-ald-medium
  python texto_a_mp3.py "Good morning" -m google -l en --lento
  python texto_a_mp3.py --web                         (versión en el navegador)

Si lo ejecutas sin texto, se abre la ventana de la aplicación.
"""


def _crear_parser():
    p = argparse.ArgumentParser(
        prog="texto_a_mp3",
        description="Convierte texto (o un PDF completo) en un archivo de audio MP3.",
        epilog=EJEMPLOS,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("texto", nargs="*", help="texto a convertir")
    p.add_argument("-a", "--archivo", help="leer el texto desde un archivo .txt o .pdf")
    p.add_argument("-p", "--paginas", type=_rango_paginas, metavar="DESDE-HASTA",
                   help="con un PDF, leer solo esas páginas (por ejemplo: 15-42)")
    p.add_argument("-o", "--salida",
                   help="archivo MP3 de salida (por defecto: salida.mp3, "
                        "o el nombre del archivo de texto con .mp3)")
    p.add_argument("-m", "--motor", choices=MOTORES, default="offline",
                   help="offline (voz natural sin internet, por defecto) o google")
    p.add_argument("-v", "--voz", choices=list(VOCES),
                   help="voz sin internet (por defecto, la del idioma; ver --voces)")
    p.add_argument("-l", "--idioma", default="es",
                   help="código de idioma: es, en, pt, fr... (por defecto: es)")
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
    p.add_argument("--voces", action="store_true",
                   help="mostrar las voces sin internet y cuáles ya están descargadas")
    p.add_argument("--crear-acceso-directo", action="store_true",
                   help="(Windows) crear el ícono «Texto a MP3» en el escritorio")
    return p


def _rango_paginas(valor):
    """'15-42' -> (15, 42); '7' -> (7, 7)."""
    partes = valor.replace(" ", "").split("-")
    try:
        desde, hasta = (int(partes[0]), int(partes[-1])) if len(partes) <= 2 else (0, 0)
    except ValueError:
        desde = hasta = 0
    if not 1 <= desde <= hasta:
        raise argparse.ArgumentTypeError(f"rango de páginas no válido: {valor!r} (usa por ejemplo 15-42)")
    return desde, hasta


def _nombre_salida(args):
    if args.salida:
        salida = args.salida
    elif args.archivo:
        salida = os.path.splitext(args.archivo)[0]
        if args.paginas:
            salida += " (págs. {}-{})".format(*args.paginas)
        salida += ".mp3"
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


def _mostrar_voces():
    for voz, (nombre, megas) in VOCES.items():
        estado = "descargada" if voz_descargada(voz) else f"se descarga al usarla ({megas} MB)"
        print(f"  {voz:<24} {nombre}  [{estado}]")


def _avance_terminal(fase, hechos=0, total=0, trozo=None):
    if fase == "descargando":
        mensaje = f"Descargando la voz (solo esta vez): {100 * hechos // max(total, 1)} %"
    elif fase == "preparando":
        mensaje = "Preparando la voz..."
    elif fase == "leyendo":
        mensaje = f"Leyendo el PDF: {100 * hechos // max(total, 1)} %"
    else:
        mensaje = (f"Convirtiendo: {100 * hechos // max(total, 1)} % "
                   f"({_miles(hechos)} de {_miles(total)} caracteres)")
    print("\r" + mensaje.ljust(70), end="", flush=True)


def main(argv=None):
    parser = _crear_parser()
    args = parser.parse_args(argv)

    try:
        if args.idiomas:
            _mostrar_idiomas()
            return 0
        if args.voces:
            _mostrar_voces()
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

        if args.paginas and not (args.archivo or "").lower().endswith(".pdf"):
            parser.error("--paginas solo sirve con un PDF (-a libro.pdf)")
        if args.archivo:
            texto = leer_documento(args.archivo, _avance_terminal, None,
                                   *(args.paginas or ()))
            print()
        elif args.texto:
            texto = " ".join(args.texto)
        else:  # texto recibido por una tubería:  echo "hola" | python texto_a_mp3.py
            texto = sys.stdin.read()

        if args.motor == "google":
            print(f"Convirtiendo con Google (idioma: {args.idioma})...")
        else:
            print(f"Convirtiendo sin internet (voz: {args.voz or voz_para(args.idioma)})...")
        ruta = convertir(texto, _nombre_salida(args), idioma=args.idioma,
                         lento=args.lento, motor=args.motor, voz=args.voz,
                         avance=_avance_terminal)
        print()
        tam_kb = os.path.getsize(ruta) / 1024
        print(f"Listo: {ruta} ({tam_kb:.1f} KB)")
        return 0
    except ErrorConversion as e:
        print(f"\nError: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
