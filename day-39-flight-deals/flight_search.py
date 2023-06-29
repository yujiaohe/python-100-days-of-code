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

    def query_flight_prices(self, flight_date: FlightData):
        header = {
            "apikey": API_KEY
        }

        for city in flight_date.data_manager.destination_data:
            params = {
                "fly_from": flight_date.from_iata,
                "fly_to": city["iataCode"],
                "date_from": flight_date.from_date.strftime("%d/%m/%Y"),
                "date_to": flight_date.to_date.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 5,
                "nights_in_dst_to": 7,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "CNY"
            }
            response = requests.get(url=f"{ENDPOINT}/v2/search", params=params, headers=header)
            data = response.json().get("data")
            lowest_price = city["lowestPrice"]
            flag = False
            message = ""
            if len(data) > 0:
                for item in data:
                    # print(f"{city['city']}:{item['price']}, lowestPrice {city['lowestPrice']}")
                    if item["price"] <= lowest_price:
                        flag = True
                        departure_date = item['route'][0]['local_departure'].split("T")[0]
                        back_date = item['route'][1]['local_departure'].split("T")[0]
                        message = f"Low price alert! Only ￥{item['price']} to fly from {flight_date.from_city}-{flight_date.from_iata} to {city['city']}-{city['iataCode']}, from {departure_date} to {back_date}."
                if not flag:
                    message = f"No flights meet your expected lowest price {lowest_price} for {city['city']}-{city['iataCode']}."
            else:
                message = f"No flights found for {city['city']}-{city['iataCode']}."

            notice = NotificationManager()
            notice.send_sms(message)

