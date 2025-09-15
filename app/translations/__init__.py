"""
Translation system for the YouTube downloader app
"""

import os
from typing import Dict, Any


def get_translations() -> Dict[str, Any]:
    """Get translations based on UI_LANGUAGE environment variable"""
    language = os.getenv("UI_LANGUAGE", "fr").lower()

    if language == "en":
        from .en import TRANSLATIONS
    else:
        # Default to French
        from .fr import TRANSLATIONS

    return TRANSLATIONS


def t(key: str, **kwargs) -> str:
    """
    Translate a key with optional formatting

    Args:
        key: Translation key
        **kwargs: Format arguments for string formatting

    Returns:
        Translated string with optional formatting applied
    """
    translations = get_translations()
    text = translations.get(key, f"[MISSING: {key}]")

    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError):
            return text

    return text
