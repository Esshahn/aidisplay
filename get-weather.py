import urllib.request
import json
import sys
import os
from datetime import datetime

def get_season(month):
    seasons = {
        (12, 1, 2): "winter",
        (3, 4, 5): "spring",
        (6, 7, 8): "summer",
        (9, 10, 11): "autumn"
    }
    return next(season for months, season in seasons.items() if month in months)

def convert_time_to_minutes(time_str):
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": "52.173",
        "longitude": "7.5474",
        "hourly": "temperature_2m,rain,snowfall,cloudcover,windspeed_10m",
        "daily": "sunrise,sunset",
        "timezone": "Europe/Berlin"
    }
    url_query = f"{url}?{'&'.join(f'{k}={v}' for k, v in params.items())}"

    with urllib.request.urlopen(url_query) as response:
        data = json.loads(response.read().decode())

    now = datetime.now()
    hour = now.hour
    
    weather_data = {
        "temp": data["hourly"]["temperature_2m"][hour],
        "rain": data["hourly"]["rain"][hour],
        "snow": data["hourly"]["snowfall"][hour],
        "clouds": data["hourly"]["cloudcover"][hour],
        "wind": data["hourly"]["windspeed_10m"][hour],
        "sunrise": data["daily"]["sunrise"][0].split("T")[1],
        "sunset": data["daily"]["sunset"][0].split("T")[1],
        "now_hour": hour,
        "now_minute": now.minute,
        "today": str(now),
        "season": get_season(now.month)
    }

    # Convert times to minutes for easier comparison
    now_minutes = hour * 60 + weather_data["now_minute"]
    sunrise_minutes = convert_time_to_minutes(weather_data["sunrise"])
    sunset_minutes = convert_time_to_minutes(weather_data["sunset"])

    # Add calculated fields
    weather_data.update({
        "now_as_minutes": now_minutes,
        "sunrise_as_minutes": sunrise_minutes,
        "sunset_as_minutes": sunset_minutes,
        "is_daylight": sunrise_minutes <= now_minutes <= sunset_minutes,
        "is_sunrise": abs(sunrise_minutes - now_minutes) < 60,
        "is_sunset": abs(sunset_minutes - now_minutes) < 60,
        "is_day": 7 <= hour <= 21
    })

    return weather_data

def save_weather():
    weather = get_weather()
    filepath = os.path.join(sys.path[0], "data", "weather.json")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w') as f:
        json.dump(weather, f)

if __name__ == "__main__":
    save_weather()
