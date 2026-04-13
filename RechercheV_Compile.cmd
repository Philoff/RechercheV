-- installation pip install pyinstaller
Echo  # compile le source en Exe
cd %~dp0source\RechercheV\
python -m PyInstaller --noconfirm --onefile --windowed --name "RechercheV"  %~dp0source\RechercheV\RechercheV.py
pause
