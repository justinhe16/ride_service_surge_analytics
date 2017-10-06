# to import Uber information
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

# to import package to help deal with json parsing
import json

# to import my own files that contain secrets (placed in gitignore)
import tokens

# import uber authenticationo tools
rom uber_rides.auth import AuthorizationCodeGrant

auth_flow = AuthorizationCodeGrant(
    <CLIENT_ID>,
    <SCOPES>,
    <CLIENT_SECRET>,
    <REDIRECT_URI>
)
auth_url = auth_flow.get_authorization_url()

# authorizes into Uber API Service and begins session
session = auth_flow.get_session(redirect_url)
client = UberRidesClient(session, sandbox_mode=True)
credentials = session.oauth2credential

# making a Price Estimate Uber API request, from the University of Southern
# California to Snowglobe Perspective (Dance Studio)
response = client.estimate_ride(
    start_latitude= 34.02235998929801,
    start_longitude= -118.28516006469727,
    end_latitude= 34.02733062053405,
    end_longitude= -118.03994178771973,
    seat_count=2
)
estimate = response.json.get('prices')

# some (temporary) printing to analyze API call returns
print json.dumps(estimate,sort_keys=True,indent=4, separators=(',', ': '))

for iterator in range(len(estimate)):
    print unicode(estimate[iterator].get("display_name")) + ', $' + unicode(estimate[iterator].get("low_estimate")) + ', $' + unicode(estimate[iterator].get("high_estimate"))
