def main():
  api_key = "api key"
  advice_file = "beauty_advice.json"

  weather = Weather(api_key)
  advice = BeautyAdvice(advice_file)
  ui = UserInterface(weather, advice)
  ui.run()

if __name__ == "__main__":
  main()