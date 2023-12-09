# Weather-Care: Self-care advice for the day
This is a small showcase of a beginner python project. I hope this can give others ideas for projects of their own, or allow others to take this idea and run with it further.

Weather-Care is a terminal app that takes in the days weather in a given location to give hair and skin care advice. With that information you can plan your self-care for the day accordingly.

This was made as part of a self-driven project for the Codecademy computer science track. I used the python I learned there along along with help from chatGPT to finish the project.

![alt text](https://github.com/lancerharris/Weather-Care/blob/main/app-in-action.gif "Gif of app in action")

## Python code
I wanted to apply my OOP knowledge so I split the app into three classes, UserInterface, Weather, and BeautyAdvice.
* UserInterface handles displaying the app in the terminal, taking in user input, using Weather and BeautyAdvice to get results, and displaying the results.
* The Weather class handles getting weather data from an API from OpenWeather. I'm pulling weather data for the current day.
* The BeautyAdvice class is in charge of taking weather data and comparing it to a JSON file of self-care conditions. When a condition is met it is retured as advice to the user. chatGPT was used to get the hair and skin care advice for different weather conditions.
The code also uses the python-dotenv package and a .env file to hide away my API key so that it isn't exposed in the repo.

## Possible Improvements
* Move the app to a web interface
* Somehow use another API to return self-care advice rather than relying on a hardcoded JSON file
* Add personal profiles to get self-care adviced better tailored to individuals

## Conclusion
The app is a project that was intended as a learning experience and thus isn't fully featured and break-proof. But it does serve as a starting point for something that I think would be pretty cool and useful.
If you want to try the app you can sign up for the OpenWeatherMap One Call API 3.0 to get an api key that you can drop into a .env file at the root of the app.

[Weather-Care GitHub Repository](https://github.com/lancerharris/Weather-Care)
