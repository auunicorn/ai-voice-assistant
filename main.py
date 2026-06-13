"""
AI Voice Assistant
------------------
Main entry point. Run this file to start the assistant.
"""

from assistant.listener import listen
from assistant.speaker import speak
from assistant.intent import classify_intent
from assistant.commands import handle_command


def run_assistant():
    speak("Hey there! I am your AI assistant. What can I do for you today?")
    print("\n🎤 Voice Assistant Started. Say 'exit' or 'quit' to stop.\n")

    while True:
        print("Listening...")
        user_input = listen()

        if not user_input:
            speak("Sorry, I didn't catch that. Please try again.")
            continue

        print(f"You said: {user_input}")

        # Exit condition
        if any(word in user_input.lower() for word in ["exit", "quit", "bye", "stop"]):
            speak("Goodbye! Have a great day.")
            print("Assistant stopped.")
            break

        # Classify intent and handle
        intent = classify_intent(user_input)
        response = handle_command(intent, user_input)
        print(f"Assistant: {response}")
        speak(response)


if __name__ == "__main__":
    run_assistant()
