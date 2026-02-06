@echo off
title Brecher Logistics Launcher
color 0A

echo ==========================================
echo   BRECHER LOGISTICS - SYSTEM STARTUP
echo ==========================================
echo.
echo [SCHRITT 1] Pruefe auf Updates und Bibliotheken...
echo.
:: Das hier installiert automatisch alles, was in requirements.txt steht
pip install -r requirements.txt

echo.
echo ------------------------------------------
echo [SCHRITT 2] Starte den Webserver...
echo ------------------------------------------
echo.
echo Die Webseite ist gleich erreichbar unter: http://127.0.0.1:5000
echo Zum Beenden einfach dieses Fenster schliessen.
echo.

:: Hier wird deine Python App gestartet
python app.py

:: Falls der Server abstürzt, bleibt das Fenster offen, damit man den Fehler lesen kann
pause