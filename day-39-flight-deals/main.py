from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from pprint import pprint

FROM_CITY = "Chengdu"

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

update_sheet = False
for row in data_manager.get_destination_data():
    if row["iataCode"] == "":
        update_sheet = True
        row["iataCode"] = flight_search.query_iata(row['city'])

pprint(data_manager.destination_data)
# update iata to google sheet
if update_sheet:
    data_manager.update_iata()

from_iata = flight_search.query_iata(FROM_CITY)
date_from = datetime.today() + timedelta(days=1)
date_to = date_from + timedelta(days=180)
flight_data = FlightData(FROM_CITY, from_iata, date_from, date_to, data_manager)
flight_search.query_flight_prices(flight_data)


