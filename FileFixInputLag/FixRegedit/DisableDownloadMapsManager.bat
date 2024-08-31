@echo off
setlocal

REM Создаем временный файл реестра
set "regfile=%temp%\disable_mapsbroker.reg"

echo Windows Registry Editor Version 5.00 > "%regfile%"
echo. >> "%regfile%"
echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MapsBroker] >> "%regfile%"
echo "Start"=dword:00000004 >> "%regfile%"

REM Импортируем файл реестра
reg import "%regfile%"

REM Удаляем временный файл реестра
del "%regfile%"

echo Параметры реестра успешно добавлены.
endlocal
