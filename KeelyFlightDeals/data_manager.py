import requests
SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/5ffd5b195a8cf321f012fd504093f64f/flightDeals/prices'

class DataManager:

    def __init__(self):
        self.prices = {}

    def get_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        result = response.json()
        self.prices = result['prices']

        return self.prices

    def update_iata(self):
        for city in self.prices:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)