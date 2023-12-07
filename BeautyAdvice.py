import json

class BeautyAdvice:
  def __init__(self, advice_file):
    with open(advice_file) as f:
      self.advice = json.load(f)

  def get_advice(self, weather_data):
    summary = weather_data["summary"]
    temperature = weather_data["temp"]["day"]
    pressure = weather_data["pressure"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    rain = weather_data["rain"]
    uvi = weather_data["uvi"]
    snow = weather_data["snow"]
    # more weather parameters

    # logic for weather conditions