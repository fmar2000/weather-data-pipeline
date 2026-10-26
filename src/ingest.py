import json
import os
from datetime import datetime
import requests


def fetch_weather_data():
  # Your OpenWeatherMap API Key
  API_KEY = "170a34a6480785be5f4803bbb2757157"
  city = "London"
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

  print(f"Fetching weather data for {city}...")
  response = requests.get(url)

  # Check if the request was successful (Status code 200)
  if response.status_code == 200:
    data = response.json()

    # Create a unique timestamp filename so files don't overwrite each other
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/weather_{city}_{timestamp}.json"

    # Ensure the raw directory exists
    os.makedirs("data/raw", exist_ok=True)

    # Save the JSON data to disk
    with open(filename, "w") as f:
      json.dump(data, f, indent=4)

    print(f"Success! Raw data saved to {filename}")
  else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.text)


if __name__ == "__main__":
  fetch_weather_data()