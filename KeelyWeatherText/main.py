import requests
import os
from twilio.rest import Client
from KeelyFlightDeals import config

api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC73138e50c12a533ed8f58b493aaace22"
auth_token = os.environ.get("AUTH_TOKEN")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 20.159361,
    "lon": -105.922409,
    "appid": api_key,
    "cnt": 3,
    "units": "metric"
}
response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])
# print(weather_data["list"][1]["weather"][0]["id"])
# print(weather_data["list"][2]["weather"][0]["id"])

# for x in range(0, 3):
#     if weather_data["list"][x]["weather"][0]["id"] < 700:
#         print("Bring an umbrella!")
#     else:
#         print("Dry times ahead!")

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="Bring an umbrella!.",
                from_=config.virtual_number,
                to=config.my_phone
                )

    print(message.status)
