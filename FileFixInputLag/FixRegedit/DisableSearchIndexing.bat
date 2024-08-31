@echo off
echo Windows Registry Editor Version 5.00 > temp.reg
echo. >> temp.reg

echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WSearch] >> temp.reg
echo "Start"=dword:00000004 >> temp.reg

reg import temp.reg

del temp.reg

echo Registry settings have been updated.
