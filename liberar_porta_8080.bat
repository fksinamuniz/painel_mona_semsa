@echo off
echo Liberando porta 8080 no Firewall do Windows...
netsh advfirewall firewall delete rule name="Abrir Porta 8080 (PMS)" >nul 2>&1
netsh advfirewall firewall add rule name="Abrir Porta 8080 (PMS)" dir=in action=allow protocol=TCP localport=8080
echo.
echo Porta 8080 liberada com sucesso!
echo Acesse: http://10.132.208.138:8080
echo.
pause
