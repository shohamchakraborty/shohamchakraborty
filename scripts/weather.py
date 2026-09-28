import json
import urllib.request

from scenes import SKY_COLORS, BASE_SCENE, get_weather_layer, make_bridge_lights

LAT = 22.57
LON = 88.36

# For testing: set to "clear", "cloudy", "rainy", etc. to force a scene.
# None means "use the real weather".
FORCE_SCENE = None
FORCE_DAY = None  # True = force day, False = force night, None = real


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
        return "cloudy"


def build_svg(temp, scene, is_day):
    """Stack the layers into one complete SVG card."""
    day_sky, night_sky = SKY_COLORS[scene]
    sky = day_sky if is_day else night_sky
    text_color = "#1B2A41" if is_day else "#F0F4F8"
    bridge_color = "#2B2D42" if is_day else "#6B7394"
    scene_art = BASE_SCENE.replace("#2B2D42", bridge_color)
    if not is_day:
        scene_art += make_bridge_lights()

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="150" viewBox="0 0 400 150">
  <rect x="0" y="0" width="400" height="150" fill="{sky}"/>
{scene_art}
{get_weather_layer(scene, is_day)}
  <text x="88" y="56"  font-family="monospace" font-size="28" fill="{text_color}">{temp:.1f}°C</text>
  <text x="88" y="80"  font-family="monospace" font-size="16" fill="{text_color}">Kolkata</text>
  <text x="88" y="100" font-family="monospace" font-size="16" fill="{text_color}">{scene.capitalize()}</text>
</svg>
"""


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
if FORCE_DAY is not None:
    is_day = FORCE_DAY

scene = FORCE_SCENE or get_scene(code)

svg = build_svg(temp, scene, is_day)

with open("weather-card.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Saved weather-card.svg  ({temp}°C, code {code}, {scene}, day={is_day})")