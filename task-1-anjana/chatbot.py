import datetime
import random

def upgraded_chatbot():
    # 1. Expanded Knowledge Base
    knowledge_base = {
        "hello": ["Hello there! How can I help you today? 🤖", "Hey! Glad you're here."],
        "hi": ["Hey! Glad you're here. What's on your mind?", "Hello! 😊"],
        "how are you": ["I'm just a collection of code, but I'm running perfectly! How are you?"],
        "name": ["I am Project 1: The Upgraded Logic Chatbot."],
        "help": ["I can answer basic questions. Try asking about the 'time', 'date', a 'joke', or just say 'hi'!"],
        "python": ["Python is an amazing programming language! It's what I'm written in."],
    }

    # 2. A list of fun programmer jokes
    jokes = [
        "Why do programmers wear glasses? Because they can't C#! 🤓",
        "Why did the programmer quit their job? Because they didn't get arrays. 🤣",
        "There are 10 types of people in the world: those who understand binary, and those who don't. 🤖",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡"
    ]

    print("Chatbot: Hello! I've been upgraded with smarter logic. 🚀")
    print("Type 'exit' to quit.\n")

    while True:
        # Sanitization: lowercase and strip extra spaces
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a wonderful day! 👋")
            break

        # --- DYNAMIC TEXT INTERACTION EXTRACTION ---
        # 3. Dynamic Feature: Check for Time or Date
        if "time" in user_input or "date" in user_input:
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M %p")
            current_date = now.strftime("%A, %B %d, %Y")
            print(f"Chatbot: Today is {current_date} and the current time is {current_time}. 🕒\n")
            continue

        # 4. Dynamic Feature: Tell a random joke
        if "joke" in user_input or "laugh" in user_input:
            print(f"Chatbot: {random.choice(jokes)}\n")
            continue

        # --- KEYWORD MATCHING LOGIC ---
        # 5. Check if any dictionary key exists inside the user's sentence
        matched = False
        for key in knowledge_base:
            if key in user_input:
                # Pick a random response from our list for that key to keep it fresh!
                response = random.choice(knowledge_base[key])
                print(f"Chatbot: {response}\n")
                matched = True
                break # Stop checking once we find a match

        # 6. Fallback response
        if not matched:
            print("Chatbot: I'm still learning! I didn't quite catch that. Try asking for a 'joke' or the 'time'. 🧠\n")

if __name__ == "__main__":
    upgraded_chatbot()