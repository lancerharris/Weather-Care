import requests

class Weather:
  def __init__(self, api_key):
    self.api_key = api_key
    self.base_url = "https://api.openweathermap.org/data/3.0/onecall?"
    self.base_geocode_url = "http://api.openweathermap.org/geo/1.0/direct?"
    self.units = "imperial"
    self.state = None
    self.country = None

  def get_state(self):
    return self.state
  
  def get_country(self):
    return self.country
  
  def get_weather_summary(self, weather_data):
    return weather_data["summary"]

  def get_weather_data(self, city):
    geolocation = self.get_geolocation(city)
    lat = geolocation[0]["lat"]
    lon = geolocation[0]["lon"]

    # only pull daily weather data
    exclude = "current,minutely,hourly,alerts"

    complete_url = "{base_url}&lat={lat}&lon={lon}&exclude={exclude}&units={units}&appid={api_key}".format(
      base_url=self.base_url,
      lat=lat,
      lon=lon,
      exclude=exclude,
      units=self.units,
      api_key=self.api_key
    )
    response = requests.get(complete_url)

    # return the first day of weather data
    current_day_weather = response.json()["daily"][0]
    return current_day_weather
  
  def get_geolocation(self, city, state = None, country = None):
    location = city
    if state != None:
      location += "," + state
    if country != None:
      location += "," + country

    complete_url = "{base_url}&q={location}&limit=1&appid={api_key}".format(
      base_url=self.base_geocode_url,
      location=location,
      api_key=self.api_key
    )

    response = requests.get(complete_url)
    return response.json()