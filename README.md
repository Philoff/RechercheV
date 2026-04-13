# rechercheV — Documentation

## Objectif

Ce programme est l'équivalent d'une rechercheV d'Excel, appliqué à deux fichiers .csv ou Excel

Il permet d'enrichir un fichier source (F1) avec des données provenant d'un second fichier (F2),
en établissant une correspondance ligne à ligne grâce à une clé de liaison commune aux deux fichiers.
La position des colonnes n'a aucune importance : le programme travaille avec le nom des colonnes.

---

## Principe de fonctionnement

### Les deux fichiers

**Fichier 1 — la source**
C'est le fichier de référence. Il définit la structure du fichier résultat : le résultat aura
exactement les mêmes colonnes que F1, dans le même ordre. Aucune colonne n'est ajoutée ni supprimée.

**Fichier 2 — l'enrichissement**
C'est le fichier qui fournit les données à injecter dans F1. Seules les colonnes explicitement
mappées sont utilisées ; toutes les autres colonnes de F2 sont ignorées. Aucune colonne n'est ajoutée ni supprimée.

### La clé de liaison
La clé de liaison est une colonne présente dans les deux fichiers, dont la valeur identifie
de manière unique chaque ligne.  
Pour chaque ligne de F1, le programme cherche dans F2 la ligne dont la valeur de clé correspond.
Si une correspondance est trouvée, les données mappées sont copiées dans la ligne de F1.
Si aucune correspondance n'est trouvée, la ligne est soit conservée telle quelle dans le résultat,
soit envoyée dans un fichier de rejet si l'option Faire un fichier de rejet est coché. Pour un résultat au format Excel les rejets sont placés dans un second onglet
Le test peut être en respectant la casse si l'option Comparaison sensibleà la casse est choisie ou pas si décochée.
Les lignes présentes dans F2 mais absentes de F1 sont ignorées.

### Le mapping des colonnes
Le mapping indique la liste des colonnes de F2 qui vont  remplir les colonnes de F1.
Chaque ligne de mapping est une paire : Destination (colonne de F1) ← Source (colonne de F2).
Les noms de colonnes ne sont pas nécessairement identiques entre les deux fichiers.
Plusieurs colonnes peuvent être mappées simultanément en un seul traitement.


## Interface — Les 3 blocs

### Bloc 1 · Sélection des fichiers et paramètres

- **Fichier 1 (Source)** : le fichier à enrichir, dont la structure est conservée dans le résultat.
- **Fichier 2 (Enrichissement)** : le fichier qui fournit les données à injecter.
- **Dossier résultat** : répertoire où sera écrit le fichier de sortie.
- **Nom du fichier généré** : nom du fichier résultat (ex. : resultat.csv).
- **Faire un fichier de rejet** : si coché, les lignes de F1 sans correspondance dans F2 sont
  écrites dans un fichier séparé (`<nom>_Rejet.csv`) au lieu d'être incluses dans le résultat.
- **Clé Liaison F1 / Clé Liaison F2** : nom de la colonne servant de clé dans chaque fichier.
  Les deux colonnes n'ont pas besoin de porter le même nom.
- **Comparaison sensible à la casse** : si décoché (défaut), "C009" et "c009" sont considérés
  comme identiques. Si coché, la casse doit correspondre exactement.
- **Commentaires** : zone libre pour noter le contexte du traitement (sauvegardée dans la config).

### Bloc 2 · Mapping des colonnes

Chaque ligne de mapping est une paire de champs :
  - Champ gauche : nom de la colonne de destination dans F1
  - Champ droit  : nom de la colonne source dans F2

Le bouton **+ Ajouter une ligne** permet d'ajouter autant de paires que nécessaire.
Le bouton **X** en bout de ligne supprime ce mapping.
Le bouton **Sauvegarder Configuration** enregistre tous les paramètres dans un fichier JSON
(`config_rechercheV.json`) qui sera rechargé automatiquement à la prochaine ouverture.

### Bloc 3 · Traitement et statistiques

Le bouton **Lancer l'enrichissement** déclenche le traitement. Le journal affiche en temps réel :
- la progression des étapes,
- un bilan final : nombre de lignes lues, lignes enrichies (avec %), lignes en rejet (avec %).

---

## Comportements automatiques

- **Encodage** : les fichiers CP1252 (encodage Windows courant) sont automatiquement convertis
  en UTF-8 avant traitement, puis le résultat est réencodé en CP1252 pour compatibilité Excel.
- **Archivage** : si un fichier résultat du même nom existe déjà dans le dossier de sortie,
  il est automatiquement renommé avec un horodatage (`resultat_20240315_143022.csv`)
  avant que le nouveau fichier soit écrit. Aucune donnée n'est jamais écrasée silencieusement.
- **Trim des clés** : les espaces en début et fin de valeur dans les colonnes de clé sont
  supprimés automatiquement avant comparaison (espaces parasites fréquents dans les exports).
- **Espaces internes préservés** : les espaces à l'intérieur des valeurs enrichies ne sont
  pas normalisés — la donnée est copiée telle quelle depuis F2.

## Prérequis techniques

- Python 3.8 ou supérieur
- Bibliothèques standard uniquement (tkinter, csv, json, os) — aucune installation requise
- Fichiers CSV avec séparateur point-virgule (`;`)
- Encodage UTF-8 ou CP1252 (Windows-1252)
- Pour créer un Exécutable à partir du code source, utiliser la commande : pip install pyinstaller


## Lancement

```
python rechercheV.py
```

La configuration du fichier présent dans le dossier de lancement est automatiquement rechargée au démarrage.
