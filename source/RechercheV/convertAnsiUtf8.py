import subprocess
import os
import time

# --- CONFIGURATION ---
fichier_entree = "Fichier.csv"
fichier_sortie = "sortie.csv"
mon_exe = r"C:\Chemin\Vers\VotreApplication.exe"

def detecter_et_convertir_en_utf8(chemin_fichier):
    """Détecte si le fichier est en ANSI et le convertit en UTF-8 si besoin."""
    if not os.path.exists(chemin_fichier):
        print(f"Erreur : {chemin_fichier} introuvable.")
        return

    # Lecture binaire pour tester l'encodage
    with open(chemin_fichier, 'rb') as f:
        raw_data = f.read(3)
    
    # Vérification du BOM UTF-8 (EF BB BF)
    is_utf8_bom = raw_data.startswith(b'\xef\xbb\xbf')
    
    if not is_utf8_bom:
        print(f"[{chemin_fichier}] Encodage ANSI détecté. Conversion en UTF-8...")
        # On lit en ANSI (cp1252) et on réécrit en UTF-8
        with open(chemin_fichier, 'r', encoding='cp1252') as f:
            contenu = f.read()
        with open(chemin_fichier, 'w', encoding='utf-8-sig') as f:
            f.write(contenu)
        print("Conversion réussie.")
    else:
        print(f"[{chemin_fichier}] Déjà en UTF-8.")

def convertir_en_ansi(chemin_fichier):
    """Force la conversion d'un fichier vers l'encodage ANSI."""
    if os.path.exists(chemin_fichier):
        print(f"[{chemin_fichier}] Conversion forcée vers ANSI...")
        with open(chemin_fichier, 'r', encoding='utf-8', errors='ignore') as f:
            contenu = f.read()
        with open(chemin_fichier, 'w', encoding='cp1252', errors='replace') as f:
            f.write(contenu)
        print("Conversion vers ANSI terminée.")

# --- ÉTAPE 1 : Préparation du fichier d'entrée ---
detecter_et_convertir_en_utf8(fichier_entree)

# --- ÉTAPE 2 : Lancement de l'exécutable et ATTENTE ---
if os.path.exists(mon_exe):
    print(f"Lancement de {mon_exe}...")
    try:
        # subprocess.run avec l'argument 'check=True' attend la fin du processus
        subprocess.run([mon_exe], check=True)
        print("L'exécutable s'est terminé avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"L'exécutable a renvoyé une erreur : {e}")
else:
    print(f"Erreur : Impossible de trouver l'exe à l'adresse {mon_exe}")

# --- ÉTAPE 3 : Contrôle du fichier de sortie ---
# On attend un court instant au cas où le système de fichier soit lent à libérer le verrou
time.sleep(1) 

if os.path.exists(fichier_sortie):
    convertir_en_ansi(fichier_sortie)
else:
    print(f"Alerte : Le fichier {fichier_sortie} n'a pas été généré par l'application.")