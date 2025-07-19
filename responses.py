import json

def load_responses():
    with open('responses.json', 'r') as file:
        return json.load(file)

data = load_responses()

def get_bot_response(user_input):
    user_input = user_input.lower()
    for category in data:
        for keyword in data[category]["keywords"]:
            if keyword in user_input:
                return data[category]["responses"][0]
    return data["default"]["responses"][0]
