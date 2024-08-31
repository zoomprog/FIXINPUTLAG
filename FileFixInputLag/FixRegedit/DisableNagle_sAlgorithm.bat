@echo off
echo Windows Registry Editor Version 5.00 > temp.reg
echo. >> temp.reg
echo ;Disable Nagle's Algorithm >> temp.reg
echo. >> temp.reg
echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces] >> temp.reg
echo "TcpAckFrequency"=dword:00000000 >> temp.reg
echo "TCPNoDelay"=dword:00000000 >> temp.reg

reg import temp.reg

del temp.reg

echo Registry settings have been updated.