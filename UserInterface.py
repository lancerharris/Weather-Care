class UserInterface:
  def __init__(self, weather, advice):
    self.weather = weather
    self.advice = advice

  def run(self):
    city = input("Enter your city: ")
    weather_data = self.weather.get_weather_data(city)
    advice = self.advice.get_advice(weather_data)
    print(advice)
