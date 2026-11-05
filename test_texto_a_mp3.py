"""Pruebas de texto_a_mp3. Ejecutar con:  python -m unittest -v"""

import io
import json
import os
import shutil
import sys
import tempfile
import threading
import time
import types
import unittest
import urllib.error
import urllib.request
from unittest import mock

import texto_a_mp3 as app

MP3_FALSO = b"ID3\x03\x00\x00\x00audio-de-prueba"


def _gtts_falso():
    """Módulos 'gtts' y 'gtts.tts' falsos, para probar sin internet."""
    gtts = types.ModuleType("gtts")
    gtts_tts = types.ModuleType("gtts.tts")

    class gTTSError(Exception):
        pass

    class gTTS:
        llamadas = []

        def __init__(self, texto, lang="en", slow=False):
            if lang == "xx":
                raise ValueError("Language not supported: xx")
            gTTS.llamadas.append((texto, lang, slow))

        def write_to_fp(self, archivo):
            archivo.write(MP3_FALSO)

    gtts.gTTS = gTTS
    gtts_tts.gTTSError = gTTSError
    return {"gtts": gtts, "gtts.tts": gtts_tts}


class MotorFalso:
    """Motor de voz falso: devuelve '<texto>|' por trozo y anota las pausas."""

    def __init__(self, al_convertir=None):
        self.trozos, self.pausas = [], []
        self.al_convertir = al_convertir

    def trozo(self, texto, pausa):
        if self.al_convertir:
            self.al_convertir(texto)
        self.trozos.append(texto)
        self.pausas.append(pausa)
        return texto.encode() + b"|"

    def terminar(self):
        return b"FIN"


def _hay_pymupdf():
    try:
        import pymupdf  # noqa: F401
        return True
    except ImportError:
        return False


def _crear_pdf(ruta):
    """PDF de 3 páginas con lo que estorba al escuchar un libro.

    Trae encabezado repetido, número de página, nota al pie en letra chica,
    llamada de nota en superíndice, una palabra partida con guion y un párrafo
    que sigue en la página siguiente.
    """
    import pymupdf

    paginas = [
        ["Tales modelos reflejaban las formas",
         "eventuales del dominio social. Formaban una argama-",
         "sa cultural aun después de envejecer su papel",
         "y lo hacían"],
        ["precisamente gracias al hecho de haber sido objetivadas.",
         "Todo sistema de ideas adquiere un significado general."],
        ["Tercera página con texto suficiente para el cuerpo del libro."],
    ]
    documento = pymupdf.open()
    for numero, lineas in enumerate(paginas, 12):
        pagina = documento.new_page()
        pagina.insert_text((72, 40), "Revista de Prueba · Vol. 3", fontsize=9)
        y = 100
        for linea in lineas:
            pagina.insert_text((72, y), linea, fontsize=12)
            if linea.endswith("su papel"):  # llamada de nota: un 1 chiquito y alto
                x = 72 + pymupdf.get_text_length(linea, fontsize=12)
                pagina.insert_text((x + 1, y - 5), "1", fontsize=7)
            y += 16
        pagina.insert_text((72, 740), "1 Esta es una nota al pie que no se lee.", fontsize=9)
        pagina.insert_text((300, 800), str(numero), fontsize=10)
    documento.save(ruta)
    documento.close()


class PruebasConversion(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.carpeta)

    def test_texto_vacio_da_error(self):
        with self.assertRaises(app.ErrorConversion):
            app.generar_mp3("   ")

    def test_motor_desconocido_da_error(self):
        with self.assertRaises(app.ErrorConversion):
            app.generar_mp3("hola", motor="otro")

    def test_google_guarda_mp3(self):
        modulos = _gtts_falso()
        with mock.patch.dict(sys.modules, modulos):
            salida = os.path.join(self.carpeta, "sub", "hola.mp3")
            ruta = app.convertir("  Hola mundo ", salida, idioma="es", lento=True,
                                 motor="google")
        with open(ruta, "rb") as f:
            self.assertEqual(f.read(), MP3_FALSO)
        self.assertEqual(modulos["gtts"].gTTS.llamadas[-1], ("Hola mundo", "es", True))

    def test_google_idioma_no_valido(self):
        with mock.patch.dict(sys.modules, _gtts_falso()):
            with self.assertRaisesRegex(app.ErrorConversion, "idioma"):
                app.generar_mp3("hola", idioma="xx", motor="google")

    def test_no_deja_archivo_si_falla(self):
        salida = os.path.join(self.carpeta, "fallo.mp3")
        with mock.patch.dict(sys.modules, _gtts_falso()):
            with self.assertRaises(app.ErrorConversion):
                app.convertir("hola", salida, idioma="xx", motor="google")
        self.assertEqual(os.listdir(self.carpeta), [])  # ni el MP3 ni el .parcial

    def test_avance_llega_al_final_y_marca_cada_trozo(self):
        texto = "Primer párrafo. Con dos oraciones.\n\nSegundo párrafo."
        motor = MotorFalso()
        avances = []
        with mock.patch.object(app, "_crear_motor", return_value=motor):
            audio = app.generar_mp3(texto, avance=lambda *a: avances.append(a))
        self.assertEqual(audio, b"Primer p\xc3\xa1rrafo. Con dos oraciones.|"
                                b"Segundo p\xc3\xa1rrafo.|FIN")
        hechos = [a[1] for a in avances]
        self.assertEqual(hechos, sorted(hechos))  # el medidor nunca retrocede
        self.assertEqual(avances[-1], ("convirtiendo", len(texto), len(texto), None))
        inicio, fin = avances[1][3]  # el segundo trozo es el segundo párrafo
        self.assertEqual(texto[inicio:fin], "Segundo párrafo.")
        self.assertEqual(motor.pausas, [app.PAUSA_PARRAFO, app.PAUSA_ORACION])

    def test_detener_no_deja_archivo(self):
        cancelar = threading.Event()
        salida = os.path.join(self.carpeta, "detenido.mp3")
        motor = MotorFalso(al_convertir=lambda texto: cancelar.set())
        with mock.patch.object(app, "_crear_motor", return_value=motor):
            with self.assertRaises(app.Cancelado):
                app.convertir("Uno.\n\nDos.\n\nTres.", salida, cancelar=cancelar)
        self.assertEqual(motor.trozos, ["Uno."])  # termina el trozo en curso y para
        self.assertEqual(os.listdir(self.carpeta), [])

    def test_leer_archivo_utf8_y_latin1(self):
        utf8 = os.path.join(self.carpeta, "a.txt")
        latin1 = os.path.join(self.carpeta, "b.txt")
        with open(utf8, "w", encoding="utf-8-sig") as f:
            f.write("Canción de cuna")
        with open(latin1, "w", encoding="latin-1") as f:
            f.write("Año nuevo")
        self.assertEqual(app.leer_archivo(utf8), "Canción de cuna")
        self.assertEqual(app.leer_archivo(latin1), "Año nuevo")

    def test_leer_archivo_inexistente(self):
        with self.assertRaises(app.ErrorConversion):
            app.leer_archivo(os.path.join(self.carpeta, "no-existe.txt"))


class PruebasPartir(unittest.TestCase):
    def textos(self, texto, maximo=app.TROZO_MAXIMO):
        return [texto[a:b] for a, b in app.partir_texto(texto, maximo)]

    def test_no_pierde_ni_una_palabra_y_respeta_el_maximo(self):
        texto = ("Esta es una oración de prueba, con comas; y punto. " * 40
                 + "\n\n" + "Otro párrafo. " * 50)
        trozos = self.textos(texto, maximo=120)
        self.assertEqual(" ".join(trozos).split(), texto.split())
        self.assertTrue(all(len(t) <= 120 for t in trozos))

    def test_corta_al_final_de_una_oracion(self):
        trozos = self.textos("Primera oración corta. Segunda oración un poco más larga.",
                             maximo=30)
        self.assertEqual(trozos[0], "Primera oración corta.")

    def test_parrafos_van_separados(self):
        self.assertEqual(self.textos("Uno.\n\n  \nDos.\nSigue dos."),
                         ["Uno.", "Dos.\nSigue dos."])

    def test_palabra_larguisima(self):
        trozos = self.textos("a" * 1200)
        self.assertEqual([len(t) for t in trozos], [500, 500, 200])

    def test_solo_espacios(self):
        self.assertEqual(app.partir_texto(" \n\n \t "), [])


class _RespuestaFalsa(io.BytesIO):
    def __init__(self, datos):
        super().__init__(datos)
        self.headers = {"Content-Length": str(len(datos))}


class PruebasVocesSinInternet(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.carpeta)
        parche = mock.patch.object(app, "CARPETA_VOCES", self.carpeta)
        parche.start()
        self.addCleanup(parche.stop)

    def test_voz_para_cada_idioma(self):
        self.assertEqual(app.voz_para("es"), "es_MX-claude-high")
        self.assertEqual(app.voz_para("en"), "en_US-lessac-medium")
        self.assertEqual(app.voz_para("es_MX-ald-medium"), "es_MX-ald-medium")
        with self.assertRaises(app.ErrorConversion):
            app.voz_para("ja")

    def test_descarga_la_voz_con_avance(self):
        urls, avances = [], []

        def abrir(url, timeout=None):
            urls.append(url)
            return _RespuestaFalsa(b"{}" if url.split("?")[0].endswith(".json")
                                   else b"x" * 600_000)

        with mock.patch("urllib.request.urlopen", side_effect=abrir):
            ruta = app.asegurar_voz("es_MX-ald-medium", lambda *a: avances.append(a))
        self.assertTrue(app.voz_descargada("es_MX-ald-medium"))
        self.assertEqual(os.path.getsize(ruta), 600_000)
        self.assertIn("/es/es_MX/ald/medium/es_MX-ald-medium.onnx?", urls[1])
        self.assertEqual(avances[-1], ("descargando", 600_000, 600_000, None))

    def test_descarga_cortada_no_deja_voz_rota(self):
        def abrir(url, timeout=None):
            if url.split("?")[0].endswith(".onnx"):
                raise urllib.error.URLError("sin conexión")
            return _RespuestaFalsa(b"{}")

        with mock.patch("urllib.request.urlopen", side_effect=abrir):
            with self.assertRaisesRegex(app.ErrorConversion, "internet"):
                app.descargar_voz("es_MX-ald-medium")
        self.assertFalse(app.voz_descargada("es_MX-ald-medium"))
        self.assertFalse([n for n in os.listdir(self.carpeta) if n.endswith(".descargando")])

    def test_voz_desconocida(self):
        with self.assertRaises(app.ErrorConversion):
            app.asegurar_voz("xx_XX-nadie-low")


@unittest.skipUnless(app.voz_descargada("es_MX-ald-medium"), "la voz es_MX-ald-medium no está descargada")
class PruebaPiperReal(unittest.TestCase):
    """Prueba de verdad con una voz de Piper, sin internet."""

    def test_genera_mp3(self):
        avances = []
        audio = app.generar_mp3("Hola, esto es una prueba. Sin internet.",
                                voz="es_MX-ald-medium", avance=lambda *a: avances.append(a))
        self.assertGreater(len(audio), 5000)
        self.assertEqual(audio[0], 0xFF)  # cabecera de trama MP3
        self.assertIn("preparando", [a[0] for a in avances])
        self.assertEqual(avances[-1][1], avances[-1][2])


@unittest.skipUnless(_hay_pymupdf(), "PyMuPDF no está instalado")
class PruebasPdf(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.carpeta = tempfile.mkdtemp()
        cls.pdf = os.path.join(cls.carpeta, "libro.pdf")
        _crear_pdf(cls.pdf)
        cls.paginas = []
        cls.texto = app.leer_pdf(cls.pdf, avance=lambda *a: cls.paginas.append(a))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.carpeta)

    def test_une_palabra_partida_con_guion(self):
        self.assertIn("una argamasa cultural", self.texto)

    def test_une_parrafo_que_sigue_en_otra_pagina(self):
        self.assertIn("su papel y lo hacían precisamente gracias", self.texto)

    def test_quita_encabezados_numeros_y_notas(self):
        self.assertNotIn("Revista", self.texto)
        self.assertNotIn("nota al pie", self.texto)
        for numero in ("12", "13", "14"):
            self.assertNotIn(numero, self.texto)
        self.assertNotIn("papel1", self.texto)

    def test_conserva_el_cuerpo(self):
        self.assertTrue(self.texto.startswith("Tales modelos reflejaban"))
        self.assertIn("Tercera página con texto suficiente", self.texto)

    def test_avisa_pagina_por_pagina(self):
        self.assertEqual(self.paginas, [("leyendo", n, 3, None) for n in (1, 2, 3)])

    def test_solo_algunas_paginas(self):
        self.assertEqual(app.contar_paginas(self.pdf), 3)
        texto = app.leer_pdf(self.pdf, desde=3, hasta=3)
        self.assertEqual(texto, "Tercera página con texto suficiente para el cuerpo del libro.")
        with self.assertRaises(app.ErrorConversion):
            app.leer_pdf(self.pdf, desde=5)

    def test_encabezado_con_errores_de_ocr(self):
        bloque = lambda y, texto: {"y0": y, "y1": y + 14, "lineas": [[(texto, 12.0, 0)]]}
        cuerpos = ["Los estilos de crianza influyen en la conducta de los niños.",
                   "La disciplina basada en el castigo físico tiene efectos negativos.",
                   "Los hermanos interactúan de forma positiva y también negativa.",
                   "El divorcio de los padres afecta de muchas formas al desarrollo."]
        encabezados = ["Capítulo 9 Desarrollo socioemocional", "282 Capitulo 9 Desarrollo socioemocional",
                       "Capítulo 9 Desarrollo socioemodonal", "Capítulo 9 Desarrollo socioemocional"]
        paginas = [[bloque(20, e), bloque(100, c)] for e, c in zip(encabezados, cuerpos)]
        texto = app._armar_texto(paginas)
        self.assertEqual(texto, "\n\n".join(cuerpos))

    def test_quita_renglon_revuelto_de_la_orilla(self):
        bloque = lambda y, texto: {"y0": y, "y1": y + 14, "lineas": [[(texto, 12.0, 0)]]}
        paginas = [[bloque(20, "( apitii i o o t h . - s a r i o l l o"),
                    bloque(100, "Texto normal del cuerpo, con palabras de verdad y todo.")]]
        self.assertEqual(app._armar_texto(paginas),
                         "Texto normal del cuerpo, con palabras de verdad y todo.")

    def test_quita_vinetas(self):
        bloque = {"y0": 100, "y1": 114, "lineas": [[("• Primera idea del texto principal.", 12.0, 0)]]}
        self.assertEqual(app._armar_texto([[bloque]]), "Primera idea del texto principal.")

    def test_pdf_sin_texto(self):
        import pymupdf

        ruta = os.path.join(self.carpeta, "escaneo.pdf")
        documento = pymupdf.open()
        documento.new_page().draw_rect(pymupdf.Rect(50, 50, 200, 200))
        documento.save(ruta)
        documento.close()
        with self.assertRaisesRegex(app.ErrorConversion, "escaneo"):
            app.leer_pdf(ruta)

    def test_no_borra_dialogo_corto_suelto(self):
        bloque = lambda y, texto: {"y0": y, "y1": y + 14, "lineas": [[(texto, 12.0, 0)]]}
        largo = "Un párrafo normal de la novela con bastante texto."
        paginas = [[bloque(100, "—No."), bloque(130, largo)] if n in (0, 5, 9)
                   else [bloque(100, largo + f" Página {n}.")] for n in range(10)]
        self.assertEqual(app._armar_texto(paginas).count("—No."), 3)


class PruebasLineaDeComandos(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.carpeta)
        silenciar = mock.patch("sys.stdout", new_callable=io.StringIO)
        silenciar.start()
        self.addCleanup(silenciar.stop)

    def test_convierte_texto(self):
        salida = os.path.join(self.carpeta, "saludo")
        with mock.patch.dict(sys.modules, _gtts_falso()):
            codigo = app.main(["Hola", "mundo", "-o", salida, "-m", "google"])
        self.assertEqual(codigo, 0)
        self.assertTrue(os.path.exists(salida + ".mp3"))

    def test_archivo_crea_mp3_con_mismo_nombre(self):
        txt = os.path.join(self.carpeta, "cuento.txt")
        with open(txt, "w", encoding="utf-8") as f:
            f.write("Había una vez...")
        with mock.patch.dict(sys.modules, _gtts_falso()):
            self.assertEqual(app.main(["-a", txt, "-m", "google"]), 0)
        self.assertTrue(os.path.exists(os.path.join(self.carpeta, "cuento.mp3")))

    @unittest.skipUnless(_hay_pymupdf(), "PyMuPDF no está instalado")
    def test_pdf_crea_mp3_con_mismo_nombre(self):
        pdf = os.path.join(self.carpeta, "libro.pdf")
        _crear_pdf(pdf)
        with mock.patch.object(app, "_crear_motor", return_value=MotorFalso()):
            self.assertEqual(app.main(["-a", pdf]), 0)
        with open(os.path.join(self.carpeta, "libro.mp3"), "rb") as f:
            self.assertIn(b"argamasa", f.read())

    @unittest.skipUnless(_hay_pymupdf(), "PyMuPDF no está instalado")
    def test_pdf_solo_algunas_paginas(self):
        pdf = os.path.join(self.carpeta, "libro.pdf")
        _crear_pdf(pdf)
        with mock.patch.object(app, "_crear_motor", return_value=MotorFalso()):
            self.assertEqual(app.main(["-a", pdf, "-p", "2-3"]), 0)
        with open(os.path.join(self.carpeta, "libro (págs. 2-3).mp3"), "rb") as f:
            audio = f.read()
        self.assertIn(b"Tercera", audio)
        self.assertNotIn(b"argamasa", audio)

    def test_rango_de_paginas(self):
        self.assertEqual(app._rango_paginas("15-42"), (15, 42))
        self.assertEqual(app._rango_paginas("7"), (7, 7))
        for malo in ("0-3", "9-2", "a-b", "1-2-3"):
            with self.assertRaises(Exception):
                app._rango_paginas(malo)

    def test_error_devuelve_codigo_1(self):
        with mock.patch("sys.stderr"):
            self.assertEqual(app.main(["-a", os.path.join(self.carpeta, "nada.txt")]), 1)


class PruebasWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.servidor = app.crear_servidor(0)
        cls.url = f"http://127.0.0.1:{cls.servidor.server_address[1]}"
        threading.Thread(target=cls.servidor.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.servidor.shutdown()
        cls.servidor.server_close()

    def post(self, datos, tipo="application/json"):
        peticion = urllib.request.Request(
            self.url + "/convertir", data=json.dumps(datos).encode(),
            headers={"Content-Type": tipo}, method="POST",
        )
        try:
            with urllib.request.urlopen(peticion) as r:
                return r.status, r.headers["Content-Type"], r.read()
        except urllib.error.HTTPError as e:
            return e.code, e.headers["Content-Type"], e.read()

    def test_pagina_principal(self):
        with urllib.request.urlopen(self.url + "/") as r:
            pagina = r.read().decode()
        self.assertIn("Texto a MP3", pagina)
        self.assertIn('<option value="es">Español</option>', pagina)
        self.assertIn('<option value="offline">', pagina)

    def test_convertir_devuelve_mp3(self):
        with mock.patch.object(app, "generar_mp3", return_value=MP3_FALSO) as gen:
            codigo, tipo, cuerpo = self.post(
                {"texto": "Hola", "idioma": "en", "motor": "google", "lento": True})
        self.assertEqual((codigo, tipo, cuerpo), (200, "audio/mpeg", MP3_FALSO))
        gen.assert_called_once_with("Hola", idioma="en", lento=True, motor="google")

    def test_error_devuelve_mensaje(self):
        codigo, _, cuerpo = self.post({"texto": "  "})
        self.assertEqual(codigo, 400)
        self.assertEqual(json.loads(cuerpo)["error"], "No hay texto para convertir.")

    def test_exige_json(self):
        codigo, _, _ = self.post({"texto": "hola"}, tipo="text/plain")
        self.assertEqual(codigo, 415)


class PruebasEscritorio(unittest.TestCase):
    def test_nombre_sugerido(self):
        self.assertEqual(app.nombre_sugerido("¡Hola, mamá! ¿Cómo estás hoy?"),
                         "hola-mama-como-estas-hoy.mp3")
        self.assertEqual(app.nombre_sugerido("¿¡!?"), "audio.mp3")

    def test_formatos(self):
        self.assertEqual(app._miles(81035), "81 035")
        self.assertEqual(app._duracion(20), "menos de 1 min")
        self.assertEqual(app._duracion(12 * 60), "12 min")
        self.assertEqual(app._duracion(65 * 60), "1 h 05 min")

    def test_script_acceso_directo_escapa_rutas(self):
        script = app._script_acceso_directo(
            r"C:\Users\O'Brien\Texto a MP3\.venv\Scripts\pythonw.exe",
            r"C:\Users\O'Brien\Texto a MP3\texto_a_mp3.py",
            r"C:\Users\O'Brien\Texto a MP3",
            r"C:\Users\O'Brien\Texto a MP3\icono.ico")
        self.assertNotIn('"', script)  # sin comillas dobles: seguro en la línea de comandos
        self.assertIn(r"'C:\Users\O''Brien\Texto a MP3\texto_a_mp3.py'", script)
        self.assertIn("' --ventana'", script)
        self.assertIn("IconLocation", script)
        self.assertTrue(script.endswith("Write-Output $ruta"))

    @unittest.skipIf(sys.platform == "win32", "solo aplica fuera de Windows")
    def test_acceso_directo_solo_en_windows(self):
        with self.assertRaises(app.ErrorConversion):
            app.crear_acceso_directo()


def _hay_pantalla():
    try:
        import tkinter
        tkinter.Tk().destroy()
        return True
    except Exception:
        return False


@unittest.skipUnless(_hay_pantalla(), "tkinter o la pantalla no están disponibles")
class PruebasVentana(unittest.TestCase):
    def setUp(self):
        import tkinter
        self.carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.carpeta)
        self.raiz = tkinter.Tk()
        self.addCleanup(self.raiz.destroy)
        self.ventana = app.VentanaApp(self.raiz)
        # Un error dentro de la ventana no debe abrir un aviso que espere un clic.
        self.errores = []
        self.raiz.report_callback_exception = lambda *e: self.errores.append(e[1])
        self.addCleanup(lambda: self.assertEqual(self.errores, []))

    def esperar(self):
        limite = time.monotonic() + 30
        while self.ventana._ocupada and time.monotonic() < limite:
            self.raiz.update()
        self.assertFalse(self.ventana._ocupada, "la tarea no terminó a tiempo")

    def elegir(self, combo, valor):
        combo.set(valor)
        combo.event_generate("<<ComboboxSelected>>")
        self.raiz.update()

    def test_texto_vacio_avisa(self):
        self.ventana.convertir_y_guardar()
        self.assertIn("Escribe algún texto", self.ventana.estado.cget("text"))

    def test_menu_cambia_entre_voces_e_idiomas(self):
        self.assertEqual(self.ventana.etiqueta_voz.cget("text"), "Voz")
        self.assertIn("Claude", self.ventana.voz.get())
        self.elegir(self.ventana.motor, app.NOMBRES_MOTOR["google"])
        self.assertEqual(self.ventana.etiqueta_voz.cget("text"), "Idioma")
        self.assertEqual(self.ventana.voz.get(), "Español")
        self.elegir(self.ventana.voz, "Inglés")
        self.elegir(self.ventana.motor, app.NOMBRES_MOTOR["offline"])
        self.assertIn("Claude", self.ventana.voz.get())  # recuerda cada elección
        self.elegir(self.ventana.motor, app.NOMBRES_MOTOR["google"])
        self.assertEqual(self.ventana.voz.get(), "Inglés")

    def test_convierte_guarda_y_pinta_lo_convertido(self):
        destino = os.path.join(self.carpeta, "prueba.mp3")
        self.ventana.texto.insert("1.0", "Good morning.\n\nHave a nice day.")
        self.elegir(self.ventana.motor, app.NOMBRES_MOTOR["google"])
        self.elegir(self.ventana.voz, "Inglés")
        self.ventana.lento.set(True)
        with mock.patch("tkinter.filedialog.asksaveasfilename", return_value=destino), \
             mock.patch.object(app, "_crear_motor", return_value=MotorFalso()) as crear:
            self.ventana.convertir_y_guardar()
            self.assertEqual(self.ventana.boton.cget("text"), "■  Detener")
            self.esperar()
        motor, idioma, lento = crear.call_args.args[:3]
        self.assertEqual((motor, idioma, lento), ("google", "en", True))
        with open(destino, "rb") as f:
            self.assertEqual(f.read(), b"Good morning.|Have a nice day.|FIN")
        self.assertIn("Listo", self.ventana.estado.cget("text"))
        self.assertEqual(str(self.ventana.boton_escuchar.cget("state")), "normal")
        marcado = self.ventana.texto.tag_ranges("convertido")
        self.assertEqual([str(i) for i in marcado], ["1.0", "3.16"])  # todo en verde
        self.assertEqual(str(self.ventana.texto.cget("state")), "normal")

    def test_usa_la_voz_elegida(self):
        self.ventana.texto.insert("1.0", "Hola.")
        self.elegir(self.ventana.voz, app.NOMBRES_VOZ["es_MX-ald-medium"])
        with mock.patch("tkinter.filedialog.asksaveasfilename",
                        return_value=os.path.join(self.carpeta, "v.mp3")), \
             mock.patch.object(app, "_crear_motor", return_value=MotorFalso()) as crear:
            self.ventana.convertir_y_guardar()
            self.esperar()
        motor, _, _, voz = crear.call_args.args[:4]
        self.assertEqual((motor, voz), ("offline", "es_MX-ald-medium"))

    def test_error_se_muestra(self):
        self.ventana.texto.insert("1.0", "hola")

        def fallar(texto):
            raise app.ErrorConversion("Sin conexión")

        with mock.patch("tkinter.filedialog.asksaveasfilename",
                        return_value=os.path.join(self.carpeta, "x.mp3")), \
             mock.patch.object(app, "_crear_motor", return_value=MotorFalso(fallar)):
            self.ventana.convertir_y_guardar()
            self.esperar()
        self.assertEqual(self.ventana.estado.cget("text"), "Sin conexión")
        self.assertEqual(str(self.ventana.boton_escuchar.cget("state")), "disabled")
        self.assertEqual(self.ventana.texto.tag_ranges("convertido"), ())

    def test_detener(self):
        destino = os.path.join(self.carpeta, "detenido.mp3")
        self.ventana.texto.insert("1.0", "Uno.\n\nDos.\n\nTres.")
        motor = MotorFalso(al_convertir=lambda texto: self.ventana._cancelar.set())
        with mock.patch("tkinter.filedialog.asksaveasfilename", return_value=destino), \
             mock.patch.object(app, "_crear_motor", return_value=motor):
            self.ventana.convertir_y_guardar()
            self.esperar()
        self.assertIn("detenida", self.ventana.estado.cget("text"))
        self.assertFalse(os.path.exists(destino))
        self.assertEqual(self.ventana.boton.cget("text"), "Convertir y guardar MP3…")

    def test_cancelar_dialogo_no_hace_nada(self):
        self.ventana.texto.insert("1.0", "hola")
        with mock.patch("tkinter.filedialog.asksaveasfilename", return_value=""), \
             mock.patch.object(app, "_crear_motor") as crear:
            self.ventana.convertir_y_guardar()
        crear.assert_not_called()
        self.assertFalse(self.ventana._ocupada)

    @unittest.skipUnless(_hay_pymupdf(), "PyMuPDF no está instalado")
    def test_abrir_pdf(self):
        pdf = os.path.join(self.carpeta, "libro.pdf")
        _crear_pdf(pdf)
        with mock.patch("tkinter.filedialog.askopenfilename", return_value=pdf):
            self.ventana.abrir_archivo()
            self.esperar()
        self.assertIn("argamasa", self.ventana.texto.get("1.0", "end"))
        self.assertIn("3 páginas", self.ventana.estado.cget("text"))
        self.assertEqual(self.ventana._nombre_desde_archivo, "libro.mp3")

    @unittest.skipUnless(_hay_pymupdf(), "PyMuPDF no está instalado")
    def test_pdf_largo_pregunta_las_paginas(self):
        pdf = os.path.join(self.carpeta, "libro.pdf")
        _crear_pdf(pdf)
        preguntas = []

        def pedir(nombre, total):
            preguntas.append((nombre, total))
            return (2, 3)

        self.ventana._pedir_paginas = pedir
        with mock.patch.object(app, "PAGINAS_SIN_PREGUNTAR", 2), \
             mock.patch("tkinter.filedialog.askopenfilename", return_value=pdf):
            self.ventana.abrir_archivo()
            self.esperar()
        self.assertEqual(preguntas, [("libro.pdf", 3)])
        texto = self.ventana.texto.get("1.0", "end")
        self.assertNotIn("Tales modelos", texto)
        self.assertIn("Tercera página", texto)
        self.assertIn("páginas 2 a 3 de 3", self.ventana.estado.cget("text"))
        self.assertEqual(self.ventana._nombre_desde_archivo, "libro (págs. 2-3).mp3")

    @unittest.skipUnless(_hay_pymupdf(), "PyMuPDF no está instalado")
    def test_cancelar_paginas_no_abre_nada(self):
        pdf = os.path.join(self.carpeta, "libro.pdf")
        _crear_pdf(pdf)
        self.ventana._pedir_paginas = lambda nombre, total: None
        with mock.patch.object(app, "PAGINAS_SIN_PREGUNTAR", 2), \
             mock.patch("tkinter.filedialog.askopenfilename", return_value=pdf):
            self.ventana.abrir_archivo()
        self.assertFalse(self.ventana._ocupada)
        self.assertEqual(self.ventana.texto.get("1.0", "end-1c"), "")

    def test_dialogo_de_paginas(self):
        resultado = []
        self.raiz.after(300, lambda: self._contestar_dialogo("5", "9"))
        resultado.append(self.ventana._pedir_paginas("libro.pdf", 40))
        self.assertEqual(resultado, [(5, 9)])

    def _contestar_dialogo(self, desde, hasta):
        dialogo = [w for w in self.raiz.winfo_children() if w.winfo_class() == "Toplevel"][0]
        try:
            cajas = [w for w in dialogo.winfo_children()[0].winfo_children()
                     if w.winfo_class() == "TSpinbox"]
            for caja, valor in zip(cajas, (desde, hasta)):
                caja.delete(0, "end")
                caja.insert(0, valor)
            cajas[0].focus_force()
            cajas[0].event_generate("<Return>")
        finally:
            if dialogo.winfo_exists():  # si algo falló, que la prueba no se quede esperando
                dialogo.destroy()


if __name__ == "__main__":
    unittest.main()
