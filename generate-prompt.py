import json
import sys
import random
import os


def load_json(filename):
    """Load JSON data from a file."""
    filepath = os.path.join(sys.path[0], filename)
    with open(filepath, 'r') as file:
        return json.load(file)


def save_json(filename, data):
    """Save JSON data to a file."""
    filepath = os.path.join(sys.path[0], filename)
    with open(filepath, 'w') as file:
        json.dump(data, file)


def random_string():
    """Randomly add a dramatic event to the scene."""
    events = [
        "the ship is burning in flames",
        "a huge comet is glowing in the sky",
        "a giant sea monster is attacking the ship",
        "a lighthouse can be seen in the distance",
        "another ship is attacking",
        "tentacles rise out of the water",
        "dolphins are jumping out of the water"
    ]
    return f", {random.choice(events)}" if random.randint(1, 8) == 1 else ""


def random_artist():
    """Randomly select an artistic style."""
    styles = [
        "baroque oil on canvas",
        "Andy Warhol",
        "Jackson Pollock",
        "Roy Lichtenstein",
        "Monet",
        "Piet Mondrian",
        "Gustav Klimt",
        "Leonardo DaVinci"
    ]
    return f"in the style of a {random.choice(styles)} painting" if random.randint(1, 5) == 1 else "in the style of a baroque oil on canvas painting"


def generate_prompt_weather(w):
    """Generate a weather-based prompt for an image."""
    conditions = []

    if w["rain"]:
        conditions.append("raining")
    if w["is_sunrise"]:
        conditions.append("at sunrise")
    if w["is_sunset"]:
        conditions.append("at sunset")
    if w["clouds"] <= 20:
        conditions.append("clear sky")
    if w["clouds"] >= 50:
        conditions.append("cloudy sky")
    if w["wind"] <= 5:
        conditions.append("no wind")
    if w["wind"] >= 5:
        conditions.append("wind blowing")
    if w["snow"] >= 1:
        conditions.append("snowing")
    
    conditions.append("at daylight" if w["is_daylight"] else "at night")

    if not w["is_daylight"] and w["clouds"] <= 20:
        conditions.append("bright stars shining")

    return f"A sailing ship at the sea{random_string()}, {', '.join(conditions)}, {random_artist()}"


def generate_prompt(w):
    """Generate the final prompt dictionary."""
    prompt = generate_prompt_weather(w)
    print(prompt)
    return {"prompt": prompt}


# Load weather data and generate a prompt
weather = load_json('/data/weather.json')
prompt_data = generate_prompt(weather)
save_json("/data/prompt.json", prompt_data)
