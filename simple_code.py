
"""
Weather-based sport suggestion
Rules:
  • Play when it's overcast.
  • Do NOT play when it's raining.
  • When it's sunny, play only if temperature < 20 °C.
"""

def should_play(weather: str, temperature_c: float) -> bool:
    w = weather.strip().lower()
    if w == "overcast":
        return True
    if "rain" in w:  # handles 'rainy', 'rain', 'rain & windy', etc.
        return False
    if w == "sunny":
        return temperature_c < 20
    # Default: be cautious
    return False

def suggest(weather: str, temperature_c: float, place: str | None = None) -> str:
    action = "play" if should_play(weather, temperature_c) else "do not play"
    loc = f" in {place}" if place else ""
    return f"Based on the weather{loc}, you should {action}. (weather='{weather}', temp={temperature_c}°C)"

if __name__ == "__main__":
    # Example usage — edit the values below or import the functions elsewhere.
    place = "Delhi"
    weather = "Sunny"
    temperature = 18

    print(suggest(weather, temperature, place))
