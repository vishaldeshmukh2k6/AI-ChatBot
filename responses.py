import random

responses = {
    "greetings": {
        "keywords": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey ", "Greetings!"]
    },
    "how_are_you": {
        "keywords": ["how are you", "how are you doing"],
        "responses": ["I'm doing well, thanks!", "All good here ", "Feeling great!"]
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": ["I'm PyBot ", "You can call me ChatBot", "Your AI assistant."]
    },
    "bye": {
        "keywords": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye! ", "See you again!", "Take care!"]
    },
    "default": {
        "responses": ["Sorry, I didn't understand that ", "Can you say that again?", "I'm not sure what you mean."]
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
