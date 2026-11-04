#!/bin/bash
# Doble clic para abrir Texto a MP3 (macOS). También funciona en Linux.
cd "$(dirname "$0")" || exit 1

salir_con_error() {
  echo "$1"
  read -r -p "Pulsa Enter para cerrar..."
  exit 1
}

if [ ! -x .venv/bin/python ]; then
  command -v python3 >/dev/null 2>&1 ||
    salir_con_error "No se encontró Python 3. Instálalo desde https://www.python.org/downloads/"
  echo "Preparando la aplicación por primera vez, espera un momento..."
  python3 -m venv .venv || salir_con_error "No se pudo preparar la aplicación."
fi

if ! .venv/bin/python -c "import gtts" >/dev/null 2>&1; then
  .venv/bin/python -m pip install --quiet --disable-pip-version-check -r requirements.txt ||
    salir_con_error "No se pudo instalar gTTS. Revisa tu conexión a internet."
fi

echo "No cierres esta ventana mientras uses la aplicación."
.venv/bin/python texto_a_mp3.py --web
