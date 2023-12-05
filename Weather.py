import requests

class Weather:
  def __init__(self, api_key):
    self.api_key = api_key
    self.base_url = "https://api.openweathermap.org/data/3.0/onecall?"

  def get_weather_data(self, city):
    complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city
    response = requests.get(complete_url)
    return response.json()