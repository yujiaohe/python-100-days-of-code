import requests
from datetime import datetime
import os

APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]
AUTH = os.environ["ENV_SHEETY_AUTH"]
SHEETY_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query_config = {
    "query": input("Tell me which exercise you did: "),
    "gender": "female",
    "weight_kg": 43,
    "height_cm": 156,
    "age": 32
}
response = requests.post(url=exercise_endpoint, json=query_config, headers=headers)
exercise_data = response.json()["exercises"]
# print(exercise_data)



response = requests.get(url=SHEETY_ENDPOINT)
workout_sheet = response.json()
# print(workout_sheet)


headers = {
    "Authorization": AUTH
}

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in exercise_data:
    user_input = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    post_date = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": user_input,
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=post_date, headers=headers)
    print(response.text)