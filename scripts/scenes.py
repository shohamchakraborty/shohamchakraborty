"""All the drawing pieces for the weather card, stored as SVG text."""

# Sky colour for each scene: (day colour, night colour)
SKY_COLORS = {
    "clear":  ("#7EC8E3", "#1B2440"),
    "cloudy": ("#A9C6D9", "#232B3E"),
    "foggy":  ("#C9D1D8", "#2E3440"),
    "rainy":  ("#8FA3B8", "#1E2733"),
    "stormy": ("#5C6B7A", "#141A22"),
}

# The part that never changes: bank, river, taxi, bridge
BASE_SCENE = """
  <rect x="0"   y="128" width="216" height="22" fill="#8D8574"/>
  <rect x="216" y="128" width="184" height="22" fill="#3A6EA5"/>

  <rect x="160" y="110" width="52" height="14" fill="#F2C230"/>
  <rect x="172" y="100" width="28" height="10" fill="#F2C230"/>
  <rect x="176" y="102" width="9"  height="6"  fill="#BFE3F2"/>
  <rect x="187" y="102" width="9"  height="6"  fill="#BFE3F2"/>
  <rect x="208" y="114" width="4"  height="4"  fill="#FFFFFF"/>
  <rect x="166" y="122" width="10" height="6"  fill="#1B1B1B"/>
  <rect x="196" y="122" width="10" height="6"  fill="#1B1B1B"/>

  <g fill="#2B2D42">
    <rect x="264" y="82" width="8" height="50"/>
    <rect x="360" y="82" width="8" height="50"/>
    <rect x="272" y="90"  width="8"  height="4"/>
    <rect x="280" y="94"  width="8"  height="4"/>
    <rect x="288" y="98"  width="8"  height="4"/>
    <rect x="296" y="102" width="8"  height="4"/>
    <rect x="304" y="106" width="24" height="4"/>
    <rect x="328" y="102" width="8"  height="4"/>
    <rect x="336" y="98"  width="8"  height="4"/>
    <rect x="344" y="94"  width="8"  height="4"/>
    <rect x="352" y="90"  width="8"  height="4"/>
    <rect x="256" y="96"  width="8" height="6"/>
    <rect x="248" y="102" width="8" height="6"/>
    <rect x="240" y="108" width="8" height="6"/>
    <rect x="232" y="114" width="8" height="6"/>
    <rect x="224" y="120" width="8" height="4"/>
    <rect x="368" y="96"  width="8" height="6"/>
    <rect x="376" y="102" width="8" height="6"/>
    <rect x="384" y="108" width="8" height="6"/>
    <rect x="392" y="114" width="8" height="6"/>
    <rect x="208" y="124" width="192" height="4"/>
    <rect x="291" y="102" width="2" height="22"/>
    <rect x="315" y="110" width="2" height="14"/>
    <rect x="339" y="102" width="2" height="22"/>
  </g>
  <g stroke="#2B2D42" stroke-width="2">
    <line x1="272" y1="94"  x2="291" y2="124"/>
    <line x1="291" y1="102" x2="272" y2="124"/>
    <line x1="291" y1="102" x2="315" y2="124"/>
    <line x1="315" y1="110" x2="291" y2="124"/>
    <line x1="315" y1="110" x2="339" y2="124"/>
    <line x1="339" y1="102" x2="315" y2="124"/>
    <line x1="339" y1="102" x2="360" y2="124"/>
    <line x1="360" y1="94"  x2="339" y2="124"/>
  </g>
"""

SUN = """
  <g fill="#FFD93D">
    <rect x="32" y="24" width="24" height="8"/>
    <rect x="24" y="32" width="40" height="24"/>
    <rect x="32" y="56" width="24" height="8"/>
  </g>
"""

CLOUD = """
  <g fill="#D7DEE6">
    <rect x="40" y="40" width="24" height="8"/>
    <rect x="32" y="48" width="48" height="8"/>
    <rect x="24" y="56" width="56" height="12"/>
  </g>
"""


def make_rain():
    """Build the 14 animated raindrops with a loop instead of writing them by hand."""
    drops = [
        (16, 0), (44, -0.6), (76, -0.3), (104, -0.9), (136, -0.15),
        (164, -0.75), (196, -0.45), (228, -1.05), (256, -0.2),
        (284, -0.8), (312, -0.5), (340, -1.0), (368, -0.35), (392, -0.65),
    ]
    parts = ['  <g fill="#DCEBF7" opacity="0.8">']
    for x, begin in drops:
        parts.append(
            f'    <rect x="{x}" y="-6" width="2" height="6">'
            f'<animate attributeName="y" from="-6" to="122" dur="1.2s" '
            f'begin="{begin}s" repeatCount="indefinite"/></rect>'
        )
    parts.append("  </g>")
    return "\n".join(parts)


MOON = """
  <g fill="#F4F1DE">
    <rect x="32" y="24" width="24" height="8"/>
    <rect x="24" y="32" width="40" height="24"/>
    <rect x="32" y="56" width="24" height="8"/>
  </g>
  <rect x="32" y="36" width="8" height="8" fill="#D9D4BE"/>
  <rect x="48" y="48" width="6" height="6" fill="#D9D4BE"/>
"""


def make_stars():
    """Small white squares that fade in and out at different times."""
    stars = [(120, 14, 0), (176, 22, -0.7), (232, 30, -1.4),
             (300, 16, -0.3), (350, 40, -1.1), (388, 12, -0.5), (12, 96, -0.9)]
    parts = ['  <g fill="#FFFFFF">']
    for x, y, begin in stars:
        parts.append(
            f'    <rect x="{x}" y="{y}" width="3" height="3">'
            f'<animate attributeName="opacity" values="1;0.2;1" dur="2s" '
            f'begin="{begin}s" repeatCount="indefinite"/></rect>'
        )
    parts.append("  </g>")
    return "\n".join(parts)


def make_fog():
    """Wide see-through bands that drift slowly left and right."""
    bands = [(60, 0), (84, -3), (104, -6)]
    parts = ['  <g fill="#FFFFFF" opacity="0.45">']
    for y, begin in bands:
        parts.append(
            f'    <rect x="-40" y="{y}" width="480" height="8">'
            f'<animate attributeName="x" values="-40;0;-40" dur="8s" '
            f'begin="{begin}s" repeatCount="indefinite"/></rect>'
        )
    parts.append("  </g>")
    return "\n".join(parts)


LIGHTNING = """
  <g fill="#FFE66D" opacity="0">
    <rect x="56" y="68" width="8"  height="8"/>
    <rect x="52" y="76" width="8"  height="8"/>
    <rect x="48" y="84" width="12" height="4"/>
    <rect x="52" y="88" width="8"  height="8"/>
    <rect x="48" y="96" width="8"  height="8"/>
    <animate attributeName="opacity" values="0;0;0;0;0;0;0;1;0;1;0;0"
             dur="4s" repeatCount="indefinite"/>
  </g>
  <rect x="0" y="0" width="400" height="150" fill="#FFFFFF" opacity="0">
    <animate attributeName="opacity" values="0;0;0;0;0;0;0;0.25;0;0.25;0;0"
             dur="4s" repeatCount="indefinite"/>
  </rect>
"""


def get_weather_layer(scene, is_day):
    """Pick the right pieces for this scene, day or night."""
    light = SUN if is_day else MOON + make_stars()

    if scene == "clear":
        return light
    if scene == "cloudy":
        return light + CLOUD
    if scene == "foggy":
        return make_fog()
    if scene == "rainy":
        return CLOUD + make_rain()
    if scene == "stormy":
        return CLOUD + LIGHTNING + make_rain()
    return light

def make_bridge_lights():
    """Warm lights along the deck, red lights on the towers, reflections in the river."""
    parts = []
    # Deck lights every 16 units
    for x in range(212, 400, 16):
        parts.append(f'  <rect x="{x}" y="121" width="2" height="2" fill="#FFD37A"/>')
        # Faint reflection in the water below
        parts.append(f'  <rect x="{x - 1}" y="136" width="4" height="1" fill="#FFD37A" opacity="0.4"/>')
    # Red warning lights on top of both towers
    parts.append('  <rect x="266" y="78" width="4" height="4" fill="#FF5A5A"/>')
    parts.append('  <rect x="362" y="78" width="4" height="4" fill="#FF5A5A"/>')
    return "\n".join(parts)