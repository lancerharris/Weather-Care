import json

class BeautyAdvice:
  def __init__(self, advice_file):
    with open(advice_file) as f:
      self.advice = json.load(f)

  def get_advice(self, weather_data):
    temperature = weather_data["daily"]["temp"]["day"]
    humidity = weather_data["daily"]["humidity"]
    # more weather parameters

    # logic for weather conditions