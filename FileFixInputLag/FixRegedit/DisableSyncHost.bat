@echo off

REM Отключение службы OneSyncSvc
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\OneSyncSvc" /v Start /t REG_DWORD /d 4 /f

REM Отключение службы OneSyncSvc_402ac
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\OneSyncSvc_402ac" /v Start /t REG_DWORD /d 4 /f

echo Реестр успешно обновлен.
