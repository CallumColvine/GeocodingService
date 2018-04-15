import argparse
from urllib.parse import urlencode
# from urllib.request import Request, urlopen
# from urllib import urlencode

import urllib.parse
import urllib.request
import json

''' 
ToDo:
- Call Here geocoding services                          DONE
- Call Google geocoding stuff                           DONE
- Parse input arguments for command line interface      TODO
- Enable RESTful calls on app                           TODO
'''

# Retrieved from https://developer.here.com/projects
HERE_APP_ID = 'T8Yh97KaSNVLi0pA2AXi'
HERE_APP_CODE = 'n0J58c0YsvFtUaX99I7UCQ'

# Retrieved from https://developers.google.com/maps/documentation/geocoding/start
GOOGLE_API_KEY = 'AIzaSyA-YjJR_ILnJurVXGpO2Rtk6ToE6P02djs'

# From Google Maps
MY_LAT = 49.287776
MY_LON = -123.1361665
MY_ADDRESS = '1655+Nelson+Street+Vancouver+Canada'


def callGoogleGeocode():
    lat = 0
    lon = 0
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1655%20Nelson%20Street%2C%20Vancouver%2C%20Canada&key=AIzaSyA-YjJR_ILnJurVXGpO2Rtk6ToE6P02djs'
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        page = response.read()
        # print (type(page))
        page = page.decode('utf8').replace("'", '"')
        page = json.loads(page)
        print (page)
        location = page.get("results", {})[0].get("geometry", {}).get("location")
        lat = location.get("lat")
        lon = location.get("lng")
        assert abs(lat - MY_LAT) < 0.001 
        assert abs(lon - MY_LON) < 0.001 


def callHereGeocode():
    # https://geocoder.cit.api.here.com/6.2/geocode.json
    #  ?app_id={YOUR_APP_ID}
    #  &app_code={YOUR_APP_CODE}
    #  &searchtext=200%20S%20Mathilda%20Sunnyvale%20CA
    lat = 0
    lon = 0
    url = 'https://geocoder.cit.api.here.com/6.2/geocode.json?searchtext=1655%20Nelson%20Street%2C%20Vancouver%2C%20Canada&app_id=T8Yh97KaSNVLi0pA2AXi&app_code=n0J58c0YsvFtUaX99I7UCQ&'
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        page = response.read()
        print (page)
        page = page.decode('utf8').replace("'", '"')
        page = json.loads(page)
        view = page.get("Response", {}).get("View", [])
        if len(view) > 0:
            points = view[0].get('Result', [])[0].get("Location", {}).get("NavigationPosition")[0]
            lat = points.get("Latitude")
            lon = points.get("Longitude")
    assert abs(lat - MY_LAT) < 0.0001 
    assert abs(lon - MY_LON) < 0.0001 


def main():
    print ("Hello there")
    callHereGeocode()
    callGoogleGeocode()
    print ("Sucessffully got lat/long from Here and Google")

if __name__ == "__main__": 
    main()
