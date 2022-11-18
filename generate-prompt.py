
import json
import sys


def load_json(filename):
    # load JSON
    with open(sys.path[0] + filename) as json_file:
        json_data = json.load(json_file)
    return json_data


def save_file(filename, data):
    """Save data to a file"""
    with open(sys.path[0] + filename, 'w') as file_object:
        json.dump(data, file_object)


def generate_prompt(weather):

    prompt = "Huge thunderstorm at the sea, with big waves, dark clouds and red and yellow sunlight, and a sailing ship, in the style of a baroque oil on canvas"
    return prompt


weather = load_json('/data/weather.json')
prompt = generate_prompt(weather)
save_file("/data/prompt.json", prompt)
