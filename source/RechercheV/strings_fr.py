# -*- coding: utf-8 -*-
"""
Chaînes de texte de l'interface — Français (FR)
Toute chaîne affichable doit être définie ici pour faciliter la traduction.
"""

STRINGS = {
    # --- Fenêtre ---
    "WINDOW_TITLE": "rechercheV — Enrichissement CSV : Fichier 1 / par Fichier 2",

    # --- Titres des blocs ---
    "BLOC1_TITLE": " 1. Sélection des Fichiers et Paramètres ",
    "BLOC2_TITLE": " 2. Mapping des colonnes (Destination F1 // Source F2)",
    "BLOC3_TITLE": " 3. Traitement et Statistiques ",

    # --- Labels bloc 1 ---
    "LABEL_FILE1":   "Fichier 1 (Source) :",
    "LABEL_FILE2":   "Fichier 2 (Enrichissement) :",
    "LABEL_RESULT":  "Fichier Résultat :",
    "LABEL_FORMAT":  "Format du résultat :",
    "FMT_CSV":       "CSV (.csv)",
    "FMT_XLSX":      "Excel (.xlsx)",
    "CHK_REJET":     "Faire un fichier de rejet",
    "LABEL_KEY1":    "Clé Liaison F1 :",
    "LABEL_KEY2":    "Clé Liaison F2 :",
    "CHK_CASE":      "Comparaison sensible à la casse",
    "LABEL_COMMENT": "Commentaires / Notes sur ce traitement :",

    # --- Sélecteur de langue ---
    "LABEL_LANG": "Langue :",

    # --- Boutons ---
    "BTN_ADD_ROW":   "+ Ajouter une ligne",
    "BTN_SAVE":      "💾 Sauvegarder Configuration",
    "BTN_RUN":       "🚀 LANCER L'ENRICHISSEMENT",
    "BTN_CLEAR_LOG": "🗑 Effacer le log",

    # --- Boîtes de dialogue fichier ---
    "FILETYPES_SUPPORTED": "Fichiers supportés",
    "FILETYPES_CSV":       "CSV",
    "FILETYPES_EXCEL":     "Excel",
    "FILETYPES_ALL":       "Tous",
    "INIT_FILE_RESULT":    "resultat",

    # --- Noms des feuilles Excel ---
    "SHEET_RESULT": "Résultat",
    "SHEET_REJET":  "Rejet",

    # --- Messages de log ---
    "LOG_INIT":        "> Initialisation du traitement...",
    "LOG_LOADING_F2":  "> Chargement des données fichier 2 en mémoire...",
    "LOG_START":       "> Début de l'enrichissement...",
    "LOG_RESULT_XLSX": "> Résultat Excel : {name}",
    "LOG_REJECT_SHEET":"(feuille Rejet : {count} ligne(s))",
    "LOG_SEPARATOR":   "-" * 40,
    "LOG_BILAN":       "BILAN DU TRAITEMENT :",
    "LOG_LINES_READ":  " - Lignes lues (F1)  : {count}",
    "LOG_LINES_OK":    " - Lignes enrichies  : {count} soit {pct} %",
    "LOG_LINES_REJ":   " - Lignes en rejet   : {count} soit {pct} %",
    "LOG_SUSPECT":     " - ⚠ Lignes suspectes : {count} (nombre de champs ≠ header)",
    "LOG_REJET_FILE":  "> Fichier Rejet : {name}",
    "LOG_ARCHIVED":    "! Fichier existant archivé : {name}",
    "LOG_RC_REPAIRED": "! {count} retour(s) chariot embarqué(s) réparé(s) : {name}",
    "LOG_CONFIG_SAVED":"✔ Configuration sauvegardée.",
    "LOG_LINE_WARN":   "  ⚠ Ligne {num} : {fields} champ(s) au lieu de {expected} — clé='{key}'",
    "LOG_ERROR":       "ERREUR : {msg}",

    # --- Erreurs de validation ---
    "ERR_F1_NOT_FOUND":  "Fichier 1 introuvable ou non spécifié.",
    "ERR_F2_NOT_FOUND":  "Fichier 2 introuvable ou non spécifié.",
    "ERR_RESULT_EMPTY":  "Fichier résultat non spécifié.",
    "ERR_OUT_DIR":       "Dossier résultat introuvable : {dir}",
    "ERR_NO_MAPPING":    "Aucune ligne de mapping définie.",
    "ERR_OPENPYXL":      "openpyxl non installé. Exécutez : pip install openpyxl",
    "ERR_KEY1_MISSING":  "Clé liaison '{key}' absente de F1.",
    "ERR_KEY2_MISSING":  "Clé liaison '{key}' absente de F2.",
    "ERR_SRC_MISSING":   "Source '{col}' absente de F2.",
    "ERR_DST_MISSING":   "Destination '{col}' absente de F1.",
}
