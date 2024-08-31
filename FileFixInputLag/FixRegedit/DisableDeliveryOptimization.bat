@echo off
echo Windows Registry Editor Version 5.00 > temp.reg
echo. >> temp.reg
echo [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Settings] >> temp.reg
echo "DownloadMode"=dword:00000000 >> temp.reg

reg import temp.reg

del temp.reg

echo Delivery Optimization has been disabled.

if "%1" neq "nopause" pause

