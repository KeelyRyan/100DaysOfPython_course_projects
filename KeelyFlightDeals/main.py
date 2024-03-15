#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime as dt, timedelta

tomorrow = dt.now() + timedelta(days=1)
six_month_from_today = dt.now() + timedelta(days=(6 * 30))

data = DataManager()
sheet_data = data.get_data()
flight_search = FlightSearch()

ORIGIN_IATA = "DUB"

if sheet_data[0]['iataCode'] == '':
    for flight in sheet_data:
        flight['iataCode'] = flight_search.get_code(flight["city"])

    print(sheet_data)

# data.prices = sheet_data
# data.update_iata()

for flight in sheet_data:
    flight_data = flight_search.get_flight_data(
            from_iata=ORIGIN_IATA,
            destination_iata=flight["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today)
    #print(flight_data)


    #print(flight_search.get_flight_data(flight['iataCode']))

#print(flight_data)
