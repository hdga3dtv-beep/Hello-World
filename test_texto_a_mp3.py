"""Pruebas de texto_a_mp3. Ejecutar con:  python -m unittest -v"""

import io
import json
import os
import shutil
import sys
import tempfile
import threading
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

        def save(self, ruta):
            with open(ruta, "wb") as f:
                f.write(MP3_FALSO)

    gtts.gTTS = gTTS
    gtts_tts.gTTSError = gTTSError
    return {"gtts": gtts, "gtts.tts": gtts_tts}


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
            ruta = app.convertir("  Hola mundo ", salida, idioma="es", lento=True)
        with open(ruta, "rb") as f:
            self.assertEqual(f.read(), MP3_FALSO)
        self.assertEqual(modulos["gtts"].gTTS.llamadas[-1], ("Hola mundo", "es", True))

    def test_google_idioma_no_valido(self):
        with mock.patch.dict(sys.modules, _gtts_falso()):
            with self.assertRaisesRegex(app.ErrorConversion, "idioma"):
                app.generar_mp3("hola", idioma="xx")

    def test_no_deja_archivo_si_falla(self):
        salida = os.path.join(self.carpeta, "fallo.mp3")
        with mock.patch.dict(sys.modules, _gtts_falso()):
            with self.assertRaises(app.ErrorConversion):
                app.convertir("hola", salida, idioma="xx")
        self.assertFalse(os.path.exists(salida))

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


class PruebasVoces(unittest.TestCase):
    def voz(self, id, name, languages):
        return types.SimpleNamespace(id=id, name=name, languages=languages)

    def test_prefiere_coincidencia_exacta(self):
        voces = [
            self.voz("roa/es-419", "Spanish (Latin America)", ["es-419"]),
            self.voz("roa/es", "Spanish (Spain)", ["es"]),
        ]
        self.assertEqual(app._buscar_voz(voces, "es"), "roa/es")
        self.assertEqual(app._buscar_voz(voces, "es-419"), "roa/es-419")

    def test_encuentra_voz_de_windows_por_nombre(self):
        voces = [
            self.voz("TTS_EN", "Microsoft Zira Desktop - English (United States)", []),
            self.voz("TTS_ES", "Microsoft Sabina Desktop - Spanish (Mexico)", []),
        ]
        self.assertEqual(app._buscar_voz(voces, "es"), "TTS_ES")

    def test_sin_coincidencias(self):
        voces = [self.voz("en", "English", [b"\x05en"])]
        self.assertIsNone(app._buscar_voz(voces, "es"))


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
            codigo = app.main(["Hola", "mundo", "-o", salida])
        self.assertEqual(codigo, 0)
        self.assertTrue(os.path.exists(salida + ".mp3"))

    def test_archivo_crea_mp3_con_mismo_nombre(self):
        txt = os.path.join(self.carpeta, "cuento.txt")
        with open(txt, "w", encoding="utf-8") as f:
            f.write("Había una vez...")
        with mock.patch.dict(sys.modules, _gtts_falso()):
            self.assertEqual(app.main(["-a", txt]), 0)
        self.assertTrue(os.path.exists(os.path.join(self.carpeta, "cuento.mp3")))

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


@unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg no está instalado")
class PruebaOfflineReal(unittest.TestCase):
    """Prueba de verdad con las voces del sistema (si están disponibles)."""

    def test_offline_genera_mp3(self):
        try:
            import pyttsx3
            pyttsx3.init()
        except Exception as e:
            self.skipTest(f"pyttsx3 no disponible: {e}")
        audio = app.generar_mp3("Hola, esto es una prueba.", motor="offline")
        self.assertGreater(len(audio), 1000)
        # Un MP3 empieza con una etiqueta ID3 o con una cabecera de trama.
        self.assertTrue(audio[:3] == b"ID3" or audio[0] == 0xFF)


if __name__ == "__main__":
    unittest.main()
