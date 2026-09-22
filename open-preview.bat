@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Methodos Lab HTML preview: http://127.0.0.1:8765/
start "" cmd /c "timeout /t 1 >nul & start http://127.0.0.1:8765/"
python -m http.server 8765 --bind 127.0.0.1
