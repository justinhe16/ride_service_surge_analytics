# to import Uber information
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

# to import package to help deal with json parsing
import json

# to import my own files that contain secrets (placed in gitignore)
import datetime
import pytz

import tokens

# authorizes into Uber API Service and begins session
session = Session(server_token=tokens.token)
client = UberRidesClient(session, sandbox_mode=True)

# making a Price Estimate Uber API request, from the University of Southern
# California to Snowglobe Perspective (Dance Studio)
response = client.get_price_estimates(
    start_latitude= 34.02235998929801,
    start_longitude= -118.28516006469727,
    end_latitude= 34.02733062053405,
    end_longitude= -118.03994178771973
)
estimate = response.json.get('prices')

# some (temporary) printing to analyze API call returns
# print(json.dumps(estimate,sort_keys=True,indent=4, separators=(',', ': ')))

# editing text files
f = open("ride_service_surge_analytics/results.txt", "a+")

for iterator in range(len(estimate)):
    f.write(str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y-%m-%d %H:%M:%S")) + " " + estimate[iterator].get("display_name") + ', $' + str(estimate[iterator].get("low_estimate")) + ', $' + str(estimate[iterator].get("high_estimate")))
    f.write("\n")
f.close()
