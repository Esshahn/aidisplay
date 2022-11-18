
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


def generate_prompt(w):
    weather = []
    if w["rain"] != 0:
        weather.append("raining")

    if w["is_sunrise"]:
        weather.append("at sunrise")

    if w["is_sunset"]:
        weather.append("at sunset")

    if w["clouds"] <= 20:
        weather.append("clear sky")

    if w["clouds"] >= 50:
        weather.append("cloudy sky")

    if w["wind"] <= 5:
        weather.append("no wind")

    if w["wind"] >= 5:
        weather.append("wind blowing")

    if w["is_day"]:
        weather.append("at daylight")
    else:
        weather.append("at night")

    description = "A sailing ship at the sea"
    styles = ["in the style of a baroque oil on canvas painting"]

    all_weather = ""
    for i in weather:
        all_weather += i + ","
    all_weather = all_weather[:-1]

    prompt = description + "," + all_weather + "," + styles[0]
    print(prompt)

    return prompt


weather = load_json('/data/weather.json')
prompt = generate_prompt(weather)
save_file("/data/prompt.json", prompt)
