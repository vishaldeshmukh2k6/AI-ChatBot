import json

def load_responses():
    with open('responses.json', 'r', encoding='utf-8') as file:
        return json.load(file)

data = load_responses()

def get_bot_response(user_input):
    user_input = user_input.lower()
    for category in data:
        for keyword in data[category].get("keywords", []):
            if keyword in user_input:
                return data[category].get("responses")[0]
    return data.get("default", {}).get("responses")[0]

