import random
import json

# Load responses from JSON file
with open('responses.json', 'r') as file:
    responses = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
    for intent, data in responses.items():
        if intent == "default":
            continue
        for keyword in data["keywords"]:
            if keyword in user_input:
                return random.choice(data["responses"])
    return random.choice(responses["default"]["responses"])
