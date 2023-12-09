import json

class BeautyAdvice:
  def __init__(self, advice_file):
    with open(advice_file) as f:
      self.advice = json.load(f)

  def get_advice(self, weather_data):
    temperature = weather_data["temp"]["day"]
    pressure = weather_data["pressure"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    uvi = weather_data["uvi"]

    # values that are not always present, default to 0 if not present
    rain = weather_data.get("rain", 0)
    snow = weather_data.get("snow", 0)
    
    variables = {
        "temperature": temperature,
        "atmospheric_pressure": pressure,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "UV_index": uvi,
        "rainfall": rain,
        "snowfall": snow
    }

    with open('beauty_advice.json', 'r') as file:
        conditions = json.load(file)["beauty_advice"]

    advice = []
    for condition in conditions:
      condition_items = [(k, v) for k, v in condition.items() if k in variables]
      if condition_items and all(self.check_condition(variables, key, value) for key, value in condition_items):
        advice.append((condition["condition"], condition["hair_care"], condition["skin_care"]))
        
    return advice

  def check_condition(self, variables, key, value):
    if key in {'rainfall', 'snowfall'} and variables[key] >= value['min']:
        return True
    elif key in {'temperature', 'humidity', 'wind_speed', 'UV_index', 'atmospheric_pressure'}:
       # Get the min and max values, and handle None explicitly
        min_val = value.get('min')
        max_val = value.get('max')
        min_val = float('-inf') if min_val is None else min_val
        max_val = float('inf') if max_val is None else max_val

        variable_value = variables.get(key)
        if variable_value is None:
            return False  # If the variable is not present, the condition cannot be met
        return min_val <= variable_value <= max_val
    
    return False
  