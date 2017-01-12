@echo off
cd ../

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

rem Get the user input:
set /P ttaUsername="Username: "

rem Export the environment variables:
set ttaPassword=password
set TTA_PLAYCOOKIE=%ttaUsername%
set TTA_GAMESERVER=149.56.29.153

echo ===============================
echo Starting Toontown Project Altis...
echo ppython: %PPYTHON_PATH%
echo Username: %ttaUsername%
echo Gameserver: %TTA_GAMESERVER%
echo ===============================

:goto

%PPYTHON_PATH% -m toontown.toonbase.ClientStartDist
pause

goto :goto