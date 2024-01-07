import requests
import config

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = config.TEQUILA_API_KEY

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
