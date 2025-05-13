@echo off
:loop
echo [Proceso2] %time% >> compartido.txt
findstr "Proceso1" compartido.txt > nul
if errorlevel 1 (
    echo Esperando mensaje de Proceso1...
) else (
    echo Mensaje recibido de Proceso1.
)
timeout /t 5 > nul
goto loop
