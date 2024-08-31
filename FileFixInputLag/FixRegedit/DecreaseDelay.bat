@echo off

REM Добавление параметра autodisconnect
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Parameters" /v autodisconnect /t REG_DWORD /d 0xffffffff /f

REM Добавление параметра Size
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Parameters" /v Size /t REG_DWORD /d 3 /f

REM Добавление параметра EnableOplocks
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Parameters" /v EnableOplocks /t REG_DWORD /d 0 /f

REM Добавление параметра IRPStackSize
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Parameters" /v IRPStackSize /t REG_DWORD /d 32 /f

REM Добавление параметра SharingViolationDelay
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Parameters" /v SharingViolationDelay /t REG_DWORD /d 0 /f

REM Добавление параметра SharingViolationRetries
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Parameters" /v SharingViolationRetries /t REG_DWORD /d 0 /f

echo Регистрационные параметры успешно добавлены.

if "%1" neq "nopause" pause
