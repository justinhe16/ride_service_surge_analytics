# to import package to help deal with json parsing
import json
from urllib.request import urlopen
import tokens

weather_response = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + tokens.weather_query + "&appid=" + tokens.weather_token)
print(weather_response)
weather_data = json.load(weather_response)
print(weather_data)
