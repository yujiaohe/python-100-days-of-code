import requests
import os

# MY_LAT = 30.572815
# MY_LNG = 104.066803
MY_KEY = os.environ["ENV_WEATHER_KEY"]

parameters = {
  "lat": 29.431585,
  "lon": 106.912254,
  "appid": MY_KEY,
  "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                        params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
first_12_hours = weather_data["hourly"][0:12]

will_rain = False

for item in first_12_hours:
  weather_id = item["weather"][0]['id']
  # print(type(weather_id))
  # print(weather_id)
  if weather_id < 700:
    will_rain = True

if will_rain:
  print("Bring an umbrella")
