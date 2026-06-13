"""
intent.py
---------
Keyword-based NLP intent classifier.
Maps user input → one of 10+ intent categories.
"""

# Intent keyword map — order matters (more specific first)
INTENT_KEYWORDS = {
    "greeting":     ["hello", "hi", "hey", "good morning", "good evening", "good afternoon"],
    "time":         ["time", "what time", "current time"],
    "date":         ["date", "today", "what day", "day is it"],
    "weather":      ["weather", "temperature", "rain", "sunny", "forecast", "humidity"],
    "search":       ["search", "google", "look up", "find", "who is", "what is", "tell me about"],
    "joke":         ["joke", "funny", "make me laugh", "tell me a joke"],
    "calculator":   ["calculate", "compute", "how much is", "what is", "plus", "minus", "multiply", "divide", "percent"],
    "news":         ["news", "headlines", "current events", "latest news"],
    "reminder":     ["remind", "reminder", "set alarm", "alert me"],
    "music":        ["play music", "play song", "music", "play"],
    "open":         ["open", "launch", "start"],
    "wikipedia":    ["wikipedia", "who was", "definition of", "meaning of"],
    "thanks":       ["thank", "thanks", "thank you", "great"],
    "unknown":      []   # fallback
}


def classify_intent(text):
    """
    Return the most likely intent string for the given text.
    Uses simple keyword matching (rule-based NLP).
    """
    text = text.lower()

    for intent, keywords in INTENT_KEYWORDS.items():
        if intent == "unknown":
            continue
        for kw in keywords:
            if kw in text:
                return intent

    return "unknown"
