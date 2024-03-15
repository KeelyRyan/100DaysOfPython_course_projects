import requests
import config
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = config.TEQUILA_API_KEY
TEQUILA_SEARCH_API ="https://api.tequila.kiwi.com/v2/search"

class FlightSearch:
    def __init__(self):
        self.iata = None

    def get_code(self, city_name):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "term": city_name, "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}",
                                headers=headers,
                                params=params)
        result = response.json()
        self.iata = result['locations'][0]['code']

        return self.iata

    def get_flight_data(self, from_iata, destination_iata, from_time, to_time ):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "fly_from": from_iata,
            "fly_to": destination_iata,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "EUR"

        }
        response = requests.get(url=f"{TEQUILA_SEARCH_API}",
                                headers=headers,
                                params=params)

        try:
            data = response.json()['data'][0]

        except IndexError:
            print(f"No flights found for {from_iata} to {destination_iata}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            availability=data["availability"]["seats"]
        )
        print(f"{flight_data.destination_city}: "
              f"€{flight_data.price} "
              f"Date:{flight_data.out_date} "
              f"Seats:{flight_data.availability}")

        return data