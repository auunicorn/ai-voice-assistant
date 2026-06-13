"""
speaker.py
----------
Converts text to speech using pyttsx3 (offline TTS engine).
"""

import pyttsx3

# Initialise engine once at module level
_engine = pyttsx3.init()

def _configure_engine():
    """Set voice properties."""
    voices = _engine.getProperty("voices")

    # Try to use a female voice if available
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            _engine.setProperty("voice", voice.id)
            break

    _engine.setProperty("rate", 155)    # speaking speed (words per minute)
    _engine.setProperty("volume", 1.0)  # volume (0.0 to 1.0)

_configure_engine()


def speak(text):
    """Convert text to speech and play it."""
    print(f"  [Speaking]: {text}")
    _engine.say(text)
    _engine.runAndWait()
