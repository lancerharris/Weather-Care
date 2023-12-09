class UserInterface:
  def __init__(self, weather, advice):
    self.weather = weather
    self.advice = advice

  def display_welcome_message(self):
    print('''\n
██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗      ██████╗ █████╗ ██████╗ ███████╗
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗    ██╔════╝██╔══██╗██╔══██╗██╔════╝
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝    ██║     ███████║██████╔╝█████╗  
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    ██║     ██╔══██║██╔══██╗██╔══╝  
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║    ╚██████╗██║  ██║██║  ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    \n''')
    print("This app provides you with personalized self-care advice based on the day's weather.")
    print("Simply enter your city (and optionally state and country) to get started.\n")

  def get_user_location(self, location):
    location_list = location.split(",")
    city = location_list[0].strip()
    if len(location_list) == 2:
        country = location_list[1].strip()
        state = None
    elif len(location_list) == 3:
        state = location_list[1].strip()
        country = location_list[2].strip()
    else:
        state = None
        country = None

    return city, state, country

  def display_weather_and_advice(self, city, state, country):
    weather_data = self.weather.get_weather_data(city, state, country)
    if weather_data == None:
      return
    
    weather_summary = self.weather.get_weather_summary(weather_data)
    state = self.weather.get_state()
    country = self.weather.get_country()

    advice = self.advice.get_advice(weather_data)

    if state == None and country != None:
       location_string = f"{city}, {country}"
    elif state != None and country == None:
       location_string = f"{city}, {state}"
    elif state == None and country == None:
       location_string = f"{city}"
    else:
       location_string = f"{city}, {state}, {country}"
       
    print(f"\nWeather Summary for {location_string}: {weather_summary}\n")
    print("Self-Care Advice:")
    if len(advice) == 0:
        print("  - Weather conditions do not warrant any specialized hair or skin care.")
    else:
      for condition, hair_care, skin_care in advice:
        print(f"  - Condition: {condition}")
        print(f"    Hair Care: {hair_care}")
        print(f"    Skin Care: {skin_care}\n")

  def process_user_input(self, user_input):
    if user_input == 'quit':
      print("Thank you for using the Weather-Based self-care Advice App. Goodbye!")
      return True
    return False

  def run(self):
    self.display_welcome_message()
    print("Now let's get your location. You can enter the following combinations: [city], [city, country], [city, state, country]. You can also type 'quit' to quit.")
    location = input("location: ").strip()
    
    while True:
      quit_app = self.process_user_input(location)
      if quit_app:
        break

      city, state, country = self.get_user_location(location)

      if city == None:
        break

      self.display_weather_and_advice(city, state, country)

      # Ask the user if they want to check another location or quit
      location = input("Enter another location or type 'quit' to quit: ").strip()
 
