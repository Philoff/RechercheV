# README — rechercheV demo files
# Join key: client_id (F1) ↔ client_id (F2) — semicolon separator (;)

╔══════════════════════════════════════════════════════════════════════════╗
║  FILE 1 (demo_fichier1.csv) — 19 data rows                              ║
║  FILE 2 (demo_fichier2.csv) — 18 data rows + extra columns              ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE01 — Standard enrichment                                            │
│ F1 rows: C001 to C010  |  Matching F2 rows: C001 to C010               │
│ Suggested mapping: ville←city  code_postal←cp  contrat←contrat_type    │
│ Expected result: 10 enriched rows, ZZZZ and YYYY remain empty           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE02 — Reject file                                                    │
│ Same data as CASE01 + enable the "Create a reject file" option          │
│ Expected result:                                                        │
│   - out_result.csv       → 10 rows (C001–C010 enriched)                │
│   - out_result_Rejet.csv →  2 rows (ZZZZ, YYYY not found in F2)        │
│ Note: C011 in F2 is orphaned (absent from F1) → silently ignored        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE03 — Case-insensitive (option unchecked = default)                  │
│ F1 row: C009 (UPPERCASE)  |  F2 row: c009 (lowercase)                  │
│ Expected result: ville = Rennes  (match despite case difference)        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE04 — Case-sensitive (option checked)                                │
│ F1 row: C009 (UPPERCASE)  |  F2 row: c009 (lowercase)                  │
│ Expected result: ville = ""  (no match, cases differ)                   │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE05 — Trimming of stray spaces on the F1 key                        │
│ F1 rows:                                                                │
│   "  PCE001  " (spaces before AND after)  → expected: ville = Paris    │
│   " PCE002"   (leading space)             → expected: ville = Lyon      │
│   "PCE003 "   (trailing space)            → expected: ville = Marseille │
│   "PCE004"    (clean key)                 → expected: ville = Bordeaux  │
│ F2 key: PCE001 to PCE004 with no spaces                                 │
│ Expected result: all 4 rows enriched thanks to strip()                  │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE06 — Internal spaces in enriched values                             │
│ F1 rows: R01, R02, R03                                                  │
│ Values in F2 containing multiple internal spaces:                       │
│   R01 lib = "Saint  Germain  en  Laye"  (double spaces)                 │
│   R02 adresse = "5   place   de   la   République"  (triple spaces)     │
│ Expected result: internal spaces PRESERVED as-is (not normalised)       │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE07 — Multiple mapping (5 simultaneous columns)                      │
│ Map: ville←city  code_postal←cp  contrat←contrat_type                  │
│      segment←segment_client  + one 5th column of your choice           │
│ Expected result: all mapped columns enriched in a single pass           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE08 — Empty F1 (header only, 0 data rows)                           │
│ Not covered by these demo files (edge case — test manually)             │
│ Create an F1 with only the header row                                   │
│ Expected result: result file created with 0 data rows                   │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE09 — CP1252 encoding auto-converted                                 │
│ Not covered by these demo files (UTF-8 encoding used here by default)   │
│ Save demo_fichier1.csv in CP1252 to test automatic conversion           │
│ Expected result: accented characters correctly read and written          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE10 — Archiving a pre-existing result file                           │
│ Run a first enrichment → generates out_result.csv                       │
│ Re-run without changing parameters                                      │
│ Expected result:                                                        │
│   - out_result_YYYYMMDD_HHMMSS.csv → old version archived               │
│   - out_result.csv → freshly generated new file                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE11 — Key absent from F1 → clean error without crash                │
│ Use demo files, type "nonexistent_column" as the F1 key                 │
│ Expected result: "ERROR: Join key '...' not found in F1" in the log,   │
│ no result file created, program remains active                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE12 — Selective loading: unmapped F2 columns ignored                 │
│ Map only: ville←city  segment←segment_client                           │
│ F2 also contains: region, lib, adresse, com, colonne_inutile_A/B       │
│ Expected result: these columns DO NOT appear in the result              │
│ (the result has exactly the same columns as F1)                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CASE13 — Result structure identical to F1                               │
│ Map all available columns                                               │
│ Expected result: the result file has EXACTLY the same columns as F1,   │
│ in the same order — no column added or removed                          │
└─────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════
QUICK CONFIGURATION TO RUN CASES 01 TO 07 + 10 TO 13
══════════════════════════════════════════════════════════════════════════
  File 1        : demo_fichier1.csv
  File 2        : demo_fichier2.csv
  Key F1        : client_id
  Key F2        : client_id
  Recommended base mapping:
      ville          ← city
      code_postal    ← cp
      contrat        ← contrat_type
      segment        ← segment_client
