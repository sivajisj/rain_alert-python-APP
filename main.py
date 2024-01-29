import requests

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC02183d8d305c2c694344132b5b3ef716'
auth_token = 'bbf135d7389543bc109f1e9fe2e346de'

api_key = "8cb142b779b80b81d347bf515604b686"
url = f"http://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": "17.440081",
    "lon" : "78.348915",
    "appid": api_key,
    "cnt":4
}
response = requests.get(url,params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(response.status_code)
# print(weather_data)
will_rain = False
for data in weather_data["list"]:
    condition_code = data["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to  bring an  ☔.",
        from_='+12053963189',
        to='+917032891144'
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Get ready for some sunshine today! Don't forget your ☀️ and stay cool.️.",
        from_='+12053963189',
        to='+917032891144'
    )









