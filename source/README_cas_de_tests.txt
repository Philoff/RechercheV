# README — Fichiers de démonstration rechercheV
# Clé de liaison : client_id (F1) ↔ client_id (F2) — séparateur point-virgule (;)

╔══════════════════════════════════════════════════════════════════════════╗
║  FICHIER 1 (demo_fichier1.csv) — 19 lignes de données                   ║
║  FICHIER 2 (demo_fichier2.csv) — 18 lignes de données + colonnes extras ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS01 — Enrichissement standard                                         │
│ Lignes F1 : C001 à C010  |  Lignes F2 correspondantes : C001 à C010     │
│ Mapping suggéré : ville←city  code_postal←cp  contrat←contrat_type      │
│ Résultat attendu : 10 lignes enrichies, ZZZZ et YYYY restent vides       │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS02 — Fichier de rejet                                                │
│ Même données que CAS01 + activer l'option "Fichier de rejet"            │
│ Résultat attendu :                                                       │
│   - out_resultat.csv       → 10 lignes (C001–C010 enrichies)            │
│   - out_resultat_Rejet.csv →  2 lignes (ZZZZ, YYYY non trouvées dans F2)│
│ Note : C011 dans F2 est orphelin (absent de F1) → ignoré silencieusement│
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS03 — Insensible à la casse (option décochée = défaut)                │
│ Ligne F1 : C009 (MAJUSCULE)  |  Ligne F2 : c009 (minuscule)            │
│ Résultat attendu : ville = Rennes  (match malgré la différence de casse)│
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS04 — Sensible à la casse (option cochée)                             │
│ Ligne F1 : C009 (MAJUSCULE)  |  Ligne F2 : c009 (minuscule)            │
│ Résultat attendu : ville = "" (pas de match, les casses diffèrent)      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS05 — Trim des espaces parasites sur la clé F1                        │
│ Lignes F1 :                                                              │
│   "  PCE001  " (espaces avant ET après)  → attendu: ville = Paris       │
│   " PCE002"   (espace avant)             → attendu: ville = Lyon        │
│   "PCE003 "   (espace après)             → attendu: ville = Marseille   │
│   "PCE004"    (clé propre)               → attendu: ville = Bordeaux    │
│ Clé F2 : PCE001 à PCE004 sans espaces                                   │
│ Résultat attendu : les 4 lignes sont enrichies grâce au strip()         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS06 — Espaces internes dans les valeurs enrichies                     │
│ Lignes F1 : R01, R02, R03                                               │
│ Valeurs dans F2 contenant des espaces multiples internes :              │
│   R01 lib = "Saint  Germain  en  Laye"  (doubles espaces)               │
│   R02 adresse = "5   place   de   la   République"  (triples espaces)   │
│ Résultat attendu : espaces internes PRÉSERVÉS tels quels (pas normalisés)│
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS07 — Mapping multiple (5 colonnes simultanées)                       │
│ Mapper : ville←city  code_postal←cp  contrat←contrat_type              │
│          segment←segment_client  + une 5e colonne au choix              │
│ Résultat attendu : toutes les colonnes mappées enrichies en un seul pass│
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS08 — F1 vide (header seul, 0 ligne de données)                       │
│ Non couvert par ces fichiers de démo (cas limite à tester manuellement) │
│ Créer un F1 avec uniquement la ligne d'en-tête                          │
│ Résultat attendu : fichier résultat créé avec 0 ligne de données        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS09 — Encodage CP1252 auto-converti                                   │
│ Non couvert par ces fichiers de démo (encodage UTF-8 par défaut ici)    │
│ Sauvegarder demo_fichier1.csv en CP1252 pour tester la conversion auto  │
│ Résultat attendu : caractères accentués correctement lus et écrits      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS10 — Archivage d'un fichier résultat préexistant                     │
│ Lancer un 1er enrichissement → génère out_resultat.csv                  │
│ Relancer sans changer les paramètres                                     │
│ Résultat attendu :                                                       │
│   - out_resultat_YYYYMMDD_HHMMSS.csv → ancienne version archivée        │
│   - out_resultat.csv → nouveau fichier fraîchement généré               │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS11 — Clé absente de F1 → erreur propre sans crash                   │
│ Utiliser les fichiers de démo, saisir "colonne_inexistante" comme clé F1│
│ Résultat attendu : message "ERREUR : Clé liaison '...' absente de F1"  │
│ dans le log, aucun fichier résultat créé, programme toujours actif      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS12 — Chargement sélectif : colonnes non mappées de F2 ignorées       │
│ Mapper uniquement : ville←city  segment←segment_client                  │
│ F2 contient aussi : region, lib, adresse, com, colonne_inutile_A/B      │
│ Résultat attendu : ces colonnes N'APPARAISSENT PAS dans le résultat     │
│ (le résultat a exactement les mêmes colonnes que F1)                    │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CAS13 — Structure du résultat identique à F1                            │
│ Mapper toutes les colonnes disponibles                                   │
│ Résultat attendu : le fichier résultat a EXACTEMENT les mêmes colonnes  │
│ que F1, dans le même ordre — aucune colonne ajoutée ou supprimée        │
└─────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════
CONFIGURATION RAPIDE POUR LANCER LES CAS 01 À 07 + 10 à 13
══════════════════════════════════════════════════════════════════════════
  Fichier 1     : demo_fichier1.csv
  Fichier 2     : demo_fichier2.csv
  Clé F1        : client_id
  Clé F2        : client_id
  Mapping de base recommandé :
      ville          ← city
      code_postal    ← cp
      contrat        ← contrat_type
      segment        ← segment_client
