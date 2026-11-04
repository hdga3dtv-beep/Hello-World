@echo off
rem Doble clic para abrir Texto a MP3 (Windows).
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
if not errorlevel 1 goto abrir
".venv\Scripts\python.exe" -m pip install --quiet --disable-pip-version-check -r requirements.txt
if errorlevel 1 goto error

:abrir
echo No cierres esta ventana mientras uses la aplicacion.
".venv\Scripts\python.exe" texto_a_mp3.py --web
if errorlevel 1 pause
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
