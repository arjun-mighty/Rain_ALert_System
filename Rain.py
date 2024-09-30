# Rain Alert

import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Your api key"

account_sid = "Your sid"
auth_token = "Your token"


weather_params = {
    "lat": 20,
    "lon": 20,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.raise_for_status)

weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True

if will_rain:
  
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="verified  number",
        to="your mobile num"
    )
    print(message.status)
