@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo  Methodos Basic ??? ???? (?? ?? A?B)
echo  http://127.0.0.1:5180/
echo.
where node >nul 2>&1
if errorlevel 1 (
  echo Node.js ? ?????. https://nodejs.org
  start "" "%~dp0guide\index.html"
  pause
  exit /b 1
)
start "" http://127.0.0.1:5180/
npx --yes serve -l 5180 guide
pause
