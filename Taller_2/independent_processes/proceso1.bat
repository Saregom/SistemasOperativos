@echo off
:loop
echo Hola desde el proceso 1 >> archivo1.txt
timeout /t 4 > nul
goto loop
