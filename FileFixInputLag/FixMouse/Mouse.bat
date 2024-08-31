@echo off
:: Check for administrative permissions
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~dp0%~nx0' -Verb RunAs"
    exit /b
)

:: Run the Python script
python FileFixInputLag\FixMouse\FixMouse.py
