"""
commands.py
-----------
Handles each recognised intent and returns a response string.
Each intent maps to an independent handler function (modular design).
"""

import datetime
import random
import webbrowser
import wikipedia
import requests
import os


# ── Helpers ────────────────────────────────────────────────────────────────

def _extract_query(text, remove_words):
    """Remove trigger words from text to isolate the search query."""
    for word in remove_words:
        text = text.replace(word, "").strip()
    return text


# ── Intent Handlers ────────────────────────────────────────────────────────

def handle_greeting(text):
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning! How can I assist you today?"
    elif hour < 17:
        return "Good afternoon! What can I do for you?"
    else:
        return "Good evening! How may I help you?"


def handle_time(text):
    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}."


def handle_date(text):
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    return f"Today is {today}."


def handle_weather(text):
    """
    Returns a mock response (to use real data, plug in OpenWeatherMap API key).
    Real implementation: requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
    """
    return ("I'd need your location to fetch live weather. "
            "You can add an OpenWeatherMap API key in commands.py to enable this feature.")


def handle_search(text):
    query = _extract_query(text, ["search", "google", "look up", "find"])
    if query:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)
        return f"Searching Google for: {query}"
    return "What would you like me to search for?"


def handle_joke(text):
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the AI go to school? To improve its learning rate!",
        "What do you call a computer that sings? A Dell!",
        "Why was the math book sad? It had too many problems.",
        "I told my computer I needed a break. Now it won't stop sending me Kit Kat ads."
    ]
    return random.choice(jokes)


def handle_calculator(text):
    """Simple expression evaluator for arithmetic queries."""
    # Replace spoken words with symbols
    replacements = {
        "plus": "+", "add": "+", "added to": "+",
        "minus": "-", "subtract": "-",
        "multiply": "*", "times": "*", "multiplied by": "*",
        "divide": "/", "divided by": "/",
        "percent of": "*0.01*",
        "what is": "", "calculate": "", "compute": "", "how much is": ""
    }
    expr = text.lower()
    for word, symbol in replacements.items():
        expr = expr.replace(word, symbol)

    # Keep only safe characters
    safe_expr = ""
    for ch in expr:
        if ch in "0123456789+-*/.() ":
            safe_expr += ch

    safe_expr = safe_expr.strip()
    if not safe_expr:
        return "I couldn't parse that calculation. Try saying something like 'calculate 25 plus 17'."

    try:
        result = eval(safe_expr)
        return f"The answer is {round(result, 4)}."
    except Exception:
        return "I had trouble computing that. Please rephrase."


def handle_news(text):
    """
    Returns mock response. Plug in NewsAPI key for live headlines.
    Real implementation: requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}")
    """
    return ("Live news requires a NewsAPI key. "
            "Visit newsapi.org to get a free key and update commands.py.")


def handle_reminder(text):
    return ("Reminder feature noted! For a full implementation, "
            "you can use the 'schedule' Python library to trigger reminders at set times.")


def handle_wikipedia(text):
    query = _extract_query(text, ["wikipedia", "who was", "who is", "definition of", "meaning of", "tell me about"])
    if not query:
        return "What would you like me to look up on Wikipedia?"
    try:
        summary = wikipedia.summary(query, sentences=2, auto_suggest=True)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There are multiple results for {query}. Can you be more specific?"
    except wikipedia.exceptions.PageError:
        return f"I couldn't find a Wikipedia page for {query}."
    except Exception:
        return "I had trouble fetching that from Wikipedia."


def handle_music(text):
    webbrowser.open("https://open.spotify.com")
    return "Opening Spotify for you!"


def handle_open(text):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "browser": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com"
    }
    for app, command in apps.items():
        if app in text:
            if command.startswith("http"):
                webbrowser.open(command)
            else:
                os.system(command)
            return f"Opening {app}."
    return "I'm not sure which application to open. Try saying 'open YouTube' or 'open calculator'."


def handle_thanks(text):
    responses = [
        "You're welcome! Happy to help.",
        "Glad I could assist!",
        "Anytime! Let me know if you need anything else.",
        "Of course! That's what I'm here for."
    ]
    return random.choice(responses)


def handle_unknown(text):
    return ("I'm not sure how to help with that yet. "
            "Try asking me the time, date, a joke, to search something, or a calculation.")


# ── Router ─────────────────────────────────────────────────────────────────

HANDLERS = {
    "greeting":   handle_greeting,
    "time":       handle_time,
    "date":       handle_date,
    "weather":    handle_weather,
    "search":     handle_search,
    "joke":       handle_joke,
    "calculator": handle_calculator,
    "news":       handle_news,
    "reminder":   handle_reminder,
    "wikipedia":  handle_wikipedia,
    "music":      handle_music,
    "open":       handle_open,
    "thanks":     handle_thanks,
    "unknown":    handle_unknown,
}


def handle_command(intent, text):
    """Route intent to the correct handler and return response."""
    handler = HANDLERS.get(intent, handle_unknown)
    return handler(text)
