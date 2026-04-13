# -*- coding: utf-8 -*-
"""
Module d'internationalisation / Internationalization module.

Usage:
    import i18n
    i18n.set_lang("fr")   # ou "en"
    label = i18n.S["LABEL_FILE1"]

Langues disponibles / Available languages: "fr", "en"
"""

from strings_fr import STRINGS as _FR
from strings_en import STRINGS as _EN

_LANGS = {
    "fr": _FR,
    "en": _EN,
}

_current_lang: str = "fr"
S: dict = _FR


def set_lang(lang: str) -> None:
    """Active la langue donnée. Retombe sur 'fr' si inconnue."""
    global _current_lang, S
    _current_lang = lang if lang in _LANGS else "fr"
    S = _LANGS[_current_lang]


def get_lang() -> str:
    """Retourne le code de la langue active ('fr' ou 'en')."""
    return _current_lang


def available_langs() -> list:
    """Retourne la liste des codes de langue disponibles."""
    return list(_LANGS.keys())
