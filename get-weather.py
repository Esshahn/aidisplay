import urllib.request
import json
import sys
from datetime import datetime

# https://open-meteo.com/en/docs#latitude=52.173&longitude=7.5474&hourly=temperature_2m,precipitation,rain,snowfall,cloudcover,windspeed_10m&daily=sunrise,sunset&timezone=Europe%2FBerlin
# https://replicate.com/pricing


def get_weather():
    url_query = f"https://api.open-meteo.com/v1/forecast?latitude=52.173&longitude=7.5474&hourly=temperature_2m,rain,snowfall,cloudcover,windspeed_10m&daily=sunrise,sunset&timezone=Europe%2FBerlin"

    with urllib.request.urlopen(url_query) as url:
        data = json.loads(url.read().decode())

    month = datetime.now().month
    hour = datetime.now().hour
    minute = datetime.now().minute

    d = {
        "temp": data["hourly"]["temperature_2m"][hour],
        "rain": data["hourly"]["rain"][hour],
        "snow": data["hourly"]["snowfall"][hour],
        "clouds": data["hourly"]["cloudcover"][hour],
        "wind": data["hourly"]["windspeed_10m"][hour],
        "sunrise": data["daily"]["sunrise"][0].split("T")[1],
        "sunset": data["daily"]["sunset"][0].split("T")[1],
        "now_hour": hour,
        "now_minute": minute,
        "now_as_minutes": hour * 60 + minute,
        "today": str(datetime.now())
    }

    if month in [9, 10, 11]:
        d["season"] = "autumn"
    if month in [12, 1, 2]:
        d["season"] = "winter"
    if month in [3, 4, 5]:
        d["season"] = "spring"
    if month in [6, 7, 8]:
        d["season"] = "summer"

    d["sunrise_as_minutes"] = int(d["sunrise"].split(":")[0]) * 60 + \
        int(d["sunrise"].split(":")[1])
    d["sunset_as_minutes"] = int(d["sunset"].split(":")[0]) * 60 + \
        int(d["sunset"].split(":")[1])

    if d["now_as_minutes"] >= d["sunrise_as_minutes"] and d["now_as_minutes"] <= d["sunset_as_minutes"]:
        d["is_daylight"] = True
    else:
        d["is_daylight"] = False

    if abs(d["sunrise_as_minutes"] - d["now_as_minutes"]) < 60:
        d["is_sunrise"] = True
    else:
        d["is_sunrise"] = False

    if abs(d["sunset_as_minutes"] - d["now_as_minutes"]) < 60:
        d["is_sunset"] = True
    else:
        d["is_sunset"] = False

    if d["now_hour"] >= 7 or d["now_hour"] <= 21:
        d["is_day"] = True
    else:
        d["is_day"] = False

    return d


def save_file(filename, data):
    """Save data to a file"""
    with open(filename, 'w') as file_object:
        json.dump(data, file_object)


weather = get_weather()
save_file(sys.path[0] + "/data/weather.json", weather)
