@echo off
echo Windows Registry Editor Version 5.00 > temp.reg
echo. >> temp.reg
echo ; Large System Cache >> temp.reg
echo. >> temp.reg
echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management] >> temp.reg
echo "LargeSystemCache"=dword:00000000 >> temp.reg

reg import temp.reg

del temp.reg

echo Registry settings have been updated.
