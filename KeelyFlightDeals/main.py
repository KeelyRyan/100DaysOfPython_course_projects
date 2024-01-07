#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

import pprint

data = DataManager()
sheet_data = data.get_data()
#print(sheet_data)

flight_search = FlightSearch()

if sheet_data[0]['iataCode'] == '':
    for flight in sheet_data:
        flight['iataCode'] = flight_search.get_code(flight["city"])

    print(sheet_data)

data.prices = sheet_data
data.update_iata()

