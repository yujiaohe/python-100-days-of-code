import os

API_KEY = os.environ.get("KIWI_API_KEY")


class FlightData:

    def __init__(self, price, from_city, from_airport, to_city, to_airport, departure_date, return_date, stop_overs=0, via_city=""):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.departure_date = departure_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city




