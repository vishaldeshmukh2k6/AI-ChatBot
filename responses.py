import random

responses = {
    "greetings": {
        "keywords": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey", "Greetings!"]
    },
    "how_are_you": {
        "keywords": ["how are you", "how are you doing"],
        "responses": ["I'm doing well, thanks!", "All good here", "Feeling great!"]
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": ["I'm PyBot", "You can call me ChatBot", "Your AI assistant."]
    },
    "bye": {
        "keywords": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "See you again!", "Take care!"]
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "No problem!", "Anytime!"]
    },
    "age": {
        "keywords": ["your age", "how old are you"],
        "responses": ["I was launched recently!", "Age doesn't matter to an AI!", "I'm timeless."]
    },
    "weather": {
        "keywords": ["weather", "is it raining", "sunny"],
        "responses": ["Looks clear today!", "Might rain later!", "Check your weather app to be sure."]
    },
    "joke": {
        "keywords": ["joke", "make me laugh", "funny"],
        "responses": ["Why don’t scientists trust atoms? Because they make up everything!", "What’s orange and sounds like a parrot? A carrot!"]
    },
    "time": {
        "keywords": ["time", "current time", "what time is it"],
        "responses": ["Time is relative!", "It's time to code!", "Check your device clock."]
    },
    "date": {
        "keywords": ["date", "today's date"],
        "responses": ["Check your calendar!", "It's a beautiful day today!", "Time flies, doesn't it?"]
    },
    "language": {
        "keywords": ["language", "what language you speak"],
        "responses": ["I understand Python, but I speak human too!", "I speak your language."]
    },
    "creator": {
        "keywords": ["who created you", "your creator"],
        "responses": ["I was created by developers!", "A team of coders brought me to life."]
    },
    "help": {
        "keywords": ["help", "assist", "support"],
        "responses": ["How can I help you?", "I’m here to assist!", "Need something?"]
    },
    "food": {
        "keywords": ["food", "hungry", "what to eat"],
        "responses": ["Pizza is always a good idea!", "How about some noodles?", "Try something healthy!"]
    },
    "hobby": {
        "keywords": ["your hobby", "what do you do for fun"],
        "responses": ["I like chatting with you!", "Solving puzzles and processing data."]
    },
    "location": {
        "keywords": ["where are you", "your location"],
        "responses": ["I'm in the cloud!", "Everywhere and nowhere at once."]
    },
    "music": {
        "keywords": ["music", "song", "play music"],
        "responses": ["I can't sing, but I can suggest songs!", "Try your favorite playlist."]
    },
    "movie": {
        "keywords": ["movie", "film", "watch something"],
        "responses": ["How about a sci-fi movie?", "I recommend The Matrix!", "Anything with robots is great."]
    },
    "sleep": {
        "keywords": ["sleep", "tired", "go to bed"],
        "responses": ["Sleep well!", "Good night!", "Rest is important."]
    },
    "default": {
        "responses": ["Sorry, I didn't understand that.", "Can you say that again?", "I'm not sure what you mean."]
    }
}

def get_response(user_input):
    user_input = user_input.lower()

    for intent in responses:
        if intent == "default":
            continue
        for keyword in responses[intent]["keywords"]:
            if keyword in user_input:
                return random.choice(responses[intent]["responses"])
    return random.choice(responses["default"]["responses"])
