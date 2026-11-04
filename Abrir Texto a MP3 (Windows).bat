@echo off
rem Doble clic para preparar Texto a MP3 y crear su icono en el escritorio (Windows).
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" goto preparar

set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY where python >nul 2>nul && set "PY=python"
if not defined PY goto sinpython
echo Preparando la aplicacion por primera vez, espera un momento...
%PY% -m venv .venv
if errorlevel 1 goto error

:preparar
".venv\Scripts\python.exe" -c "import gtts" >nul 2>nul
if not errorlevel 1 goto icono
echo Instalando lo necesario, espera un momento...
".venv\Scripts\python.exe" -m pip install --quiet --disable-pip-version-check -r requirements.txt
if errorlevel 1 goto error

:icono
rem Crea (o actualiza) el icono "Texto a MP3" del escritorio.
".venv\Scripts\python.exe" texto_a_mp3.py --crear-acceso-directo
if errorlevel 1 pause

rem Abre la ventana de la aplicacion sin la ventana negra.
start "" ".venv\Scripts\pythonw.exe" texto_a_mp3.py --ventana
exit /b

:sinpython
echo No se encontro Python 3.
echo Instalalo desde https://www.python.org/downloads/ y vuelve a abrir este archivo.
pause
exit /b 1

:error
echo No se pudo preparar la aplicacion. Revisa tu conexion a internet.
pause
exit /b 1
