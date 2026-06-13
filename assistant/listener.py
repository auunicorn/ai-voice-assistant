"""
listener.py
-----------
Handles microphone input and converts speech to text
using Google Speech Recognition API.
"""

import speech_recognition as sr


def listen(timeout=5, phrase_limit=8):
    """
    Listen to microphone and return recognised text.
    Returns None if speech is not understood.
    """
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 350        # sensitivity to ambient noise
    recognizer.pause_threshold = 1.0         # seconds of silence to end phrase
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("  [Adjusting for ambient noise...]")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
        except sr.WaitTimeoutError:
            print("  [No speech detected within timeout]")
            return None

    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        return text.lower().strip()
    except sr.UnknownValueError:
        print("  [Could not understand audio]")
        return None
    except sr.RequestError as e:
        print(f"  [Google Speech API error: {e}]")
        return None
