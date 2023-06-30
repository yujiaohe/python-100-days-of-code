import os
import requests
from flight_data import FlightData
from notification_manager import NotificationManager

API_KEY = os.environ.get("KIWI_API_KEY")
ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:

    def query_iata(self, city):
        header = {
            "apikey": API_KEY
        }
        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=f"{ENDPOINT}/locations/query", params=params, headers=header)
        return response.json()["locations"][0]["code"]

    def query_flight_prices(self, from_iata, to_iata, from_date, to_date):
        header = {
            "apikey": API_KEY
        }
        params = {
            "fly_from": from_iata,
            "fly_to": to_iata,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CNY"
        }
        response = requests.get(url=f"{ENDPOINT}/v2/search", params=params, headers=header)
        try:
            data = response.json().get("data")[0]
        except IndexError:
            return None

        flight_data = FlightData(
            price=data["price"],
            from_city=data["cityFrom"],
            from_airport=data["flyFrom"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            to_city=data["cityTo"],
            to_airport=data["flyTo"],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        return flight_data


