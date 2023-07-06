"""
Contains functions to translate text En-Fr and Fr-En
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates input English text into French
    """
    translator = MyMemoryTranslator(source="en-US", target="fr-FR")
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates input French text into English
    """
    translator = MyMemoryTranslator(source="fr-FR", target="en-GB")
    english_text = translator.translate(french_text)
    return english_text
