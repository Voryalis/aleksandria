@echo off
setlocal
cd /d "%~dp0" || exit /b 1

py -3 -c "import sys; sys.exit(sys.version_info < (3, 9))" >nul 2>&1
if not errorlevel 1 goto run_py

python -c "import sys; sys.exit(sys.version_info < (3, 9))" >nul 2>&1
if not errorlevel 1 goto run_python

echo Python 3.9 or newer is required.
echo Install it from https://www.python.org/downloads/ and run this launcher again.
pause
exit /b 1

:run_py
py -3 game.py %*
goto finish

:run_python
python game.py %*

:finish
set "game_exit=%errorlevel%"
echo.
pause
exit /b %game_exit%
