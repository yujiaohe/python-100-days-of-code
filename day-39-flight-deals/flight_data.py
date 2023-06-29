import os
import requests
from data_manager import DataManager
from notification_manager import NotificationManager

API_KEY = os.environ.get("KIWI_API_KEY")




class FlightData:

    def __init__(self, from_city, from_iata, from_date, to_date, data_manager: DataManager):
        self.from_city = from_city
        self.from_iata = from_iata
        self.from_date = from_date
        self.to_date = to_date
        self.data_manager = data_manager




