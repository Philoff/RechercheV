# rechercheV — Documentation (English)

## Purpose

This program is the equivalent of Excel's **VLOOKUP**, applied to two CSV or Excel files.

It enriches a source file (F1) with data from a second file (F2), matching rows using a
common join key shared between the two files.
Column position does not matter: the program works exclusively with column names.

---

## How it works

### The two files

**File 1 — the source**
This is the reference file. It defines the structure of the output file: the result will have
exactly the same columns as F1, in the same order. No column is added or removed.

**File 2 — the enrichment**
This file provides the data to inject into F1. Only explicitly mapped columns are used;
all other columns in F2 are ignored. No column is added or removed.

### The join key
The join key is a column present in both files whose value uniquely identifies each row.
For each row in F1, the program looks up the matching row in F2 by key value.
If a match is found, the mapped data is copied into the F1 row.
If no match is found, the row is either kept as-is in the result, or written to a separate
reject file if the **Create a reject file** option is checked. For Excel output, rejected rows
are placed in a second sheet.
The comparison can be case-sensitive (option checked) or case-insensitive (default, unchecked).
Rows present in F2 but absent from F1 are silently ignored.

### Column mapping
The mapping defines which F2 columns fill which F1 columns.
Each mapping row is a pair: Destination (F1 column) ← Source (F2 column).
Column names do not need to be identical between the two files.
Multiple columns can be mapped simultaneously in a single run.

---

## Interface — The 3 blocks

### Block 1 · File selection & parameters

- **File 1 (Source)**: the file to enrich; its structure is preserved in the output.
- **File 2 (Enrichment)**: the file that provides the data to inject.
- **Result File**: full path (folder + filename) of the output file.
- **Create a reject file**: if checked, F1 rows with no match in F2 are written to a separate
  file (`<name>_Rejet.csv`) instead of being included in the result.
- **Join Key F1 / Join Key F2**: name of the key column in each file.
  The two columns do not need to share the same name.
- **Case-sensitive comparison**: if unchecked (default), "C009" and "c009" are treated as equal.
  If checked, case must match exactly.
- **Comments**: free-text area to note processing context (saved in the config file).

### Block 2 · Column mapping

Each mapping row is a pair of fields:
  - Left field: destination column name in F1
  - Right field: source column name in F2

The **+ Add a row** button adds as many pairs as needed.
The **X** button at the end of a row removes that mapping.
The **Save Configuration** button saves all settings to a JSON file
(`config_rechercheV.json`) which is automatically reloaded on next launch.

### Block 3 · Processing & statistics

The **Run Enrichment** button starts the process. The log displays in real time:
- step-by-step progress,
- a final summary: lines read, enriched lines (with %), rejected lines (with %).

---

## Automatic behaviours

- **Encoding**: CP1252 files (common Windows encoding) are automatically converted to UTF-8
  before processing; the output is re-encoded to CP1252 for Excel compatibility.
- **Archiving**: if an output file with the same name already exists, it is automatically
  renamed with a timestamp (`result_20240315_143022.csv`) before the new file is written.
  No data is ever silently overwritten.
- **Key trimming**: leading and trailing spaces in key column values are stripped automatically
  before comparison (stray spaces are common in data exports).
- **Internal spaces preserved**: spaces inside enriched values are not normalised — data is
  copied exactly as it appears in F2.

---

## Technical requirements

- Python 3.8 or higher
- Standard libraries only (tkinter, csv, json, os) — no additional installation required
- CSV files with semicolon separator (`;`)
- UTF-8 or CP1252 (Windows-1252) encoding
- To build a standalone executable from source: `pip install pyinstaller`

## Launch

```
python rechercheV.py
```

The configuration file located in the launch folder is automatically reloaded at startup.
