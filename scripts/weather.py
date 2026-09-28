import json
import urllib.request

LAT = 22.57
LON = 88.36


def get_scene(code):
    """Turn a weather code into one of our 5 scene names."""
    if code == 0:
        return "clear"
    elif code in (1, 2, 3):
        return "cloudy"
    elif code in (45, 48):
        return "foggy"
    elif 51 <= code <= 67 or 80 <= code <= 82:
        return "rainy"
    elif code >= 95:
        return "stormy"
    else:
        return "cloudy"  # safe fallback (e.g. snow codes)


url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LAT}&longitude={LON}"
    "&current=temperature_2m,weather_code,is_day"
    "&timezone=Asia%2FKolkata"
)

with urllib.request.urlopen(url) as response:
    data = json.load(response)

current = data["current"]
temp = current["temperature_2m"]
code = current["weather_code"]
is_day = current["is_day"] == 1

scene = get_scene(code)

print("Temperature:", temp)
print("Weather code:", code)
print("Daytime?", is_day)
print("Scene:", scene)
