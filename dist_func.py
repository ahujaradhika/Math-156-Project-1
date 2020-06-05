import json
import data
import requests

API_KEY=data.API_KEY
API_URL="https://maps.googleapis.com/maps/api/distancematrix/json?"
def get_distance(orig_lat, orig_lon, dest_lat, dest_lon):
    parameters = {
        "units": "metric",
        "origins": str(orig_lat) + ',' + str(orig_lon),
        "destinations": str(dest_lat) + ',' + str(dest_lon),
        "key": API_KEY
    }

    response = requests.get(API_URL, params=parameters)
    print(response.json()['rows'][0]['elements'][0]['distance']['value'])

# Example
get_distance(34.0640089,-118.4514482,34.065656,-118.4478412)