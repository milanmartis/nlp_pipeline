@echo off
echo === NLP Pipeline Setup ===

REM Overenie Python 3.10
py -3.10 --version
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python 3.10 not found. Please install it from https://www.python.org/downloads/release/python-3109/
    pause
    exit /b
)

REM Vytvorenie virtualenv
echo [INFO] Creating virtual environment...
py -3.10 -m venv venv

REM Aktivácia venv a inštalácia
call venv\Scripts\activate.bat
echo [INFO] Installing requirements...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo === Done! ===
echo To activate environment next time, run:
echo venv\Scripts\activate
pause