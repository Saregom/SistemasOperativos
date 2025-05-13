@echo off
:loop
echo Hola desde el proceso 2 >> archivo2.txt
timeout /t 6 > nul
goto loop
