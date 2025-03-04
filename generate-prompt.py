import json
import os
import random

EVENTS = [
    "the ship is burning in flames",
    "a huge comet is glowing in the sky",
    "a giant sea monster is attacking the ship",
    "a lighthouse can be seen in the distance",
    "another ship is attacking",
    "tentacles rise out of the water",
    "dolphins are jumping out of the water"
]

ARTISTS = [
    "baroque oil on canvas",
    "Andy Warhol",
    "Jackson Pollock",
    "Roy Lichtenstein",
    "Monet",
    "Piet Mondrian",
    "Gustav Klimt",
    "Leonardo DaVinci"
]

def load_json(filename):
    """Load JSON data from a file."""
    with open(filename, 'r') as file:
        return json.load(file)

def save_json(filename, data):
    """Save JSON data to a file."""
    with open(filename, 'w') as file:
        json.dump(data, file)

def get_random_event():
    """Add a random dramatic event with 1/8 probability."""
    return f", {random.choice(EVENTS)}" if random.randint(1, 8) == 1 else ""

def get_artistic_style():
    """Get artistic style with 1/5 probability of non-baroque."""
    return (f"in the style of a {random.choice(ARTISTS)} painting" 
            if random.randint(1, 5) == 1 
            else "in the style of a baroque oil on canvas painting")

def generate_weather_conditions(weather):
    """Generate weather condition descriptions."""
    conditions = []
    
    if weather["rain"]: conditions.append("raining")
    if weather["is_sunrise"]: conditions.append("at sunrise")
    if weather["is_sunset"]: conditions.append("at sunset")
    if weather["clouds"] <= 20: conditions.append("clear sky")
    if weather["clouds"] >= 50: conditions.append("cloudy sky")
    if weather["wind"] <= 5: conditions.append("no wind")
    if weather["wind"] >= 5: conditions.append("wind blowing")
    if weather["snow"] >= 1: conditions.append("snowing")
    
    conditions.append("at daylight" if weather["is_daylight"] else "at night")
    
    if not weather["is_daylight"] and weather["clouds"] <= 20:
        conditions.append("bright stars shining")
    
    return ", ".join(conditions)

def generate_prompt(weather):
    """Generate the complete image prompt."""
    conditions = generate_weather_conditions(weather)
    event = get_random_event()
    style = get_artistic_style()
    
    prompt = f"A sailing ship at the sea{event}, {conditions}, {style}"
    print(prompt)
    return {"prompt": prompt}

if __name__ == "__main__":
    # Setup data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    # Generate and save prompt
    weather_file = os.path.join(data_dir, "weather.json")
    prompt_file = os.path.join(data_dir, "prompt.json")
    
    weather_data = load_json(weather_file)
    prompt_data = generate_prompt(weather_data)
    save_json(prompt_file, prompt_data)
