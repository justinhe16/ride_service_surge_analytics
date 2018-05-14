# to import Uber information
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

# to import package to help deal with json parsing
import json
from urllib.request import urlopen

# to import my own files that contain secrets (placed in gitignore)
import datetime
import pytz

import tokens

# authorizes into Uber API Service and begins session
session = Session(server_token=tokens.token)
client = UberRidesClient(session, sandbox_mode=True)

# making a Price Estimate Uber API request
response = client.get_price_estimates(
    start_latitude= float(tokens.origin_lat),
    start_longitude= float(tokens.origin_long),
    end_latitude= float(tokens.destination_lat),
    end_longitude= float(tokens.destination_long)
)
price_estimate = response.json.get('prices')

weather_response = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + tokens.weather_query + "&appid=" + tokens.weather_token)
weather_data = json.load(weather_response)

traffic_response = urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + tokens.origin_lat + "," + tokens.origin_long + "&destinations=" + tokens.destination_lat + "," + tokens.destination_long + "&departure_time=now&key=" + tokens.google_distance_matrix_token)
traffic_data = json.load(traffic_response)

# used for use on automated droplet
# f = open("ride_service_surge_analytics/results.txt", "a+")

# used for use on local during testing
f = open("results.txt", "a+")

f.write(str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y-%m-%d %H:%M:%S")))
f.write("\n")
f.write(str(traffic_data['rows'][0]['elements'][0]['duration_in_traffic']['value']) + " seconds")
f.write("\n")
for i, element in enumerate(weather_data['weather']):
    if (i == len(weather_data['weather'])-1):
        f.write(element["description"])
    else:
        f.write(element["description"] + ",")
f.write("\n")
for iterator in range(len(price_estimate)):
    f.write(price_estimate[iterator].get("display_name") + ', $' + str(price_estimate[iterator].get("low_estimate")) + ', $' + str(price_estimate[iterator].get("high_estimate")))
    f.write("\n")
f.close()
