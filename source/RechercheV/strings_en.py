# -*- coding: utf-8 -*-
"""
Displayable strings — English (EN)
All displayable text must be defined here for easy translation.
"""

STRINGS = {
    # --- Window ---
    "WINDOW_TITLE": "rechercheV — CSV Enrichment: File 1 / by File 2",

    # --- Block titles ---
    "BLOC1_TITLE": " 1. File Selection & Parameters ",
    "BLOC2_TITLE": " 2. Column Mapping (Destination F1 // Source F2)",
    "BLOC3_TITLE": " 3. Processing & Statistics ",

    # --- Block 1 labels ---
    "LABEL_FILE1":   "File 1 (Source):",
    "LABEL_FILE2":   "File 2 (Enrichment):",
    "LABEL_RESULT":  "Result File:",
    "LABEL_FORMAT":  "Output format:",
    "FMT_CSV":       "CSV (.csv)",
    "FMT_XLSX":      "Excel (.xlsx)",
    "CHK_REJET":     "Create a reject file",
    "LABEL_KEY1":    "Join Key F1:",
    "LABEL_KEY2":    "Join Key F2:",
    "CHK_CASE":      "Case-sensitive comparison",
    "LABEL_COMMENT": "Comments / Notes on this process:",

    # --- Language selector ---
    "LABEL_LANG": "Language:",

    # --- Buttons ---
    "BTN_ADD_ROW":   "+ Add a row",
    "BTN_SAVE":      "💾 Save Configuration",
    "BTN_RUN":       "🚀 RUN ENRICHMENT",
    "BTN_CLEAR_LOG": "🗑 Clear log",

    # --- File dialogs ---
    "FILETYPES_SUPPORTED": "Supported files",
    "FILETYPES_CSV":       "CSV",
    "FILETYPES_EXCEL":     "Excel",
    "FILETYPES_ALL":       "All",
    "INIT_FILE_RESULT":    "result",

    # --- Excel sheet names ---
    "SHEET_RESULT": "Result",
    "SHEET_REJET":  "Rejected",

    # --- Log messages ---
    "LOG_INIT":        "> Initializing process...",
    "LOG_LOADING_F2":  "> Loading File 2 data into memory...",
    "LOG_START":       "> Starting enrichment...",
    "LOG_RESULT_XLSX": "> Excel result: {name}",
    "LOG_REJECT_SHEET":"(Reject sheet: {count} row(s))",
    "LOG_SEPARATOR":   "-" * 40,
    "LOG_BILAN":       "PROCESSING SUMMARY:",
    "LOG_LINES_READ":  " - Lines read (F1)    : {count}",
    "LOG_LINES_OK":    " - Enriched lines     : {count} i.e. {pct}%",
    "LOG_LINES_REJ":   " - Rejected lines     : {count} i.e. {pct}%",
    "LOG_SUSPECT":     " - ⚠ Suspect lines    : {count} (field count ≠ header)",
    "LOG_REJET_FILE":  "> Reject file: {name}",
    "LOG_ARCHIVED":    "! Existing file archived: {name}",
    "LOG_RC_REPAIRED": "! {count} embedded carriage return(s) repaired: {name}",
    "LOG_CONFIG_SAVED":"✔ Configuration saved.",
    "LOG_LINE_WARN":   "  ⚠ Line {num}: {fields} field(s) instead of {expected} — key='{key}'",
    "LOG_ERROR":       "ERROR: {msg}",

    # --- Validation errors ---
    "ERR_F1_NOT_FOUND":  "File 1 not found or not specified.",
    "ERR_F2_NOT_FOUND":  "File 2 not found or not specified.",
    "ERR_RESULT_EMPTY":  "Result file not specified.",
    "ERR_OUT_DIR":       "Result folder not found: {dir}",
    "ERR_NO_MAPPING":    "No mapping rows defined.",
    "ERR_OPENPYXL":      "openpyxl not installed. Run: pip install openpyxl",
    "ERR_KEY1_MISSING":  "Join key '{key}' not found in F1.",
    "ERR_KEY2_MISSING":  "Join key '{key}' not found in F2.",
    "ERR_SRC_MISSING":   "Source column '{col}' not found in F2.",
    "ERR_DST_MISSING":   "Destination column '{col}' not found in F1.",
}
