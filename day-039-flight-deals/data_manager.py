import os
import requests

ENDPOINT = os.environ.get("SHEETY_PRICES")
AUTH = os.environ.get("SHEETY_PRICES_AUTH")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        header = {
            "Authorization": AUTH
        }
        response = requests.get(url=ENDPOINT, headers=header)
        print(response.text)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_iata(self):
        header = {
            "Authorization": AUTH
        }
        for city in self.destination_data:
            put_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{ENDPOINT}/{city['id']}", json=put_data, headers=header)
            print(response.text)

