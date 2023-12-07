from dotenv import load_dotenv
import os

from Weather import Weather
from BeautyAdvice import BeautyAdvice
from UserInterface import UserInterface

load_dotenv()

def main():
  api_key = os.getenv("API_KEY")
  advice_file = "beauty_advice.json"

  weather = Weather(api_key)
  advice = BeautyAdvice(advice_file)
  ui = UserInterface(weather, advice)
  ui.run()

if __name__ == "__main__":
  main()