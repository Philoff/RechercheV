@echo off
REM ═══════════════════════════════════════════════════════════════════
REM  rechercheV — Script de lancement avec contrôle d'environnement
REM  Vérifie et installe les dépendances avant lancement
REM ═══════════════════════════════════════════════════════════════════

cd /d %~dp0
set PROG=%~dp0source\RechercheV\rechercheV.py
set PYTHON=python

echo.
echo  === rechercheV — Vérification de l'environnement ===
echo.

REM ── 1. Python disponible ? ──────────────────────────────────────────
%PYTHON% --version >nul 2>&1
if errorlevel 1 (
    echo  [ERREUR] Python n'est pas installe ou absent du PATH.
    echo  Téléchargez Python 3.8+ sur https://www.python.org/downloads/
    echo  Cochez "Add Python to PATH" lors de l'installation.
    pause
    exit /b 1
)
for /f "tokens=*" %%v in ('%PYTHON% --version 2^>^&1') do echo  [OK] %%v


REM ── 2. tkinter disponible ? (inclus dans Python standard) ───────────
%PYTHON% -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo  [ERREUR] tkinter absent. Réinstallez Python avec l'option tcl/tk cochée.
    pause
    exit /b 1
)
echo  [OK] tkinter


REM ── 3. Droits d'installation pip ────────────────────────────────────
set PIP_OPT=
net session >nul 2>&1
if errorlevel 1 (
    echo  [INFO]  Non administrateur — pip utilisera --user si nécessaire
    set PIP_OPT=--user
) else (
    echo  [OK] Droits administrateur
)


REM ── 4. openpyxl (lecture/écriture Excel .xlsx) ──────────────────────
%PYTHON% -c "import openpyxl" >nul 2>&1
if errorlevel 1 (
    echo  [INSTALL] openpyxl absent — installation en cours...
    %PYTHON% -m pip install openpyxl %PIP_OPT% --quiet
    if errorlevel 1 (
        echo  [ERREUR] Impossible d'installer openpyxl.
        echo  Essayez manuellement : python -m pip install openpyxl
        pause
        exit /b 1
    )
    echo  [OK] openpyxl installe
) else (
    echo  [OK] openpyxl
)


REM ── 5. xlrd (lecture Excel ancien format .xls) ──────────────────────
%PYTHON% -c "import xlrd" >nul 2>&1
if errorlevel 1 (
    echo  [INSTALL] xlrd absent — installation en cours...
    %PYTHON% -m pip install xlrd %PIP_OPT% --quiet
    if errorlevel 1 (
        echo  [AVERT]  xlrd non installe — les fichiers .xls ne seront pas supportes.
        REM Non bloquant : le programme fonctionne sans xlrd pour .csv et .xlsx
    ) else (
        echo  [OK] xlrd installe
    )
) else (
    echo  [OK] xlrd
)


REM ── 6. Fichier programme présent ? ──────────────────────────────────
if not exist "%PROG%" (
    echo  [ERREUR] Fichier introuvable : %PROG%
    echo  Vérifiez que rechercheV.py est bien dans source\RechercheV\
    pause
    exit /b 1
)
echo  [OK] rechercheV.py trouve


REM ── 7. Lancement ────────────────────────────────────────────────────
echo.
echo  === Lancement de rechercheV ===
echo.
%PYTHON% "%PROG%"

REM En cas d'erreur au lancement, on garde la fenêtre ouverte
if errorlevel 1 (
    echo.
    echo  [ERREUR] rechercheV s'est terminé avec une erreur.
    pause
)
