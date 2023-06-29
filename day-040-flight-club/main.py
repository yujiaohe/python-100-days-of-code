from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
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

# pprint(data_manager.destination_data)
# update iata to google sheet
if update_sheet:
    data_manager.update_iata()


# users
# data_manager.subscribe_user()
from_iata = flight_search.query_iata(FROM_CITY)
date_from = datetime.today() + timedelta(days=1)
date_to = date_from + timedelta(days=180)
for destination in sheet_data:
    flight_data = flight_search.query_flight_prices(from_iata, destination["iataCode"], date_from, date_to)
    message = ""
    try:
        if flight_data.price < destination["lowestPrice"]:
            message = f"Low price alert! Only ￥{flight_data.price} to fly from {flight_data.from_city}-{flight_data.from_airport} to {flight_data.to_city}-{flight_data.to_airport}, from {flight_data.departure_date} to {flight_data.return_date}."
            noticer = NotificationManager()
            noticer.send_sms(message)
        else:
            message = f"No flights lower than {destination['lowestPrice']} for {flight_data.to_city}."
    except AttributeError:
        message = f"No flights found for {destination['city']}."
    finally:
        print(message)

