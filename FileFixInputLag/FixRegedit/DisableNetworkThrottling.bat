@echo off
echo Windows Registry Editor Version 5.00 > temp.reg
echo. >> temp.reg
echo ; Network throttling >> temp.reg
echo ; System responsiveness >> temp.reg
echo. >> temp.reg
echo [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile] >> temp.reg
echo "NetworkThrottlingIndex"=dword:ffffffff >> temp.reg
echo "SystemResponsiveness"=dword:00000000 >> temp.reg

reg import temp.reg

del temp.reg

echo Registry settings have been updated.
