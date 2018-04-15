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
- Call Google geocoding stuff                           IN PROGRESS
- Parse input arguments for command line interface      TODO
- Enable RESTful calls on app                           TODO
'''

# Retrieved from https://developer.here.com/projects
HERE_APP_ID = 'T8Yh97KaSNVLi0pA2AXi'
HERE_APP_CODE = 'n0J58c0YsvFtUaX99I7UCQ'

# From Google Maps
MY_LAT = 49.287776
MY_LON = -123.1361665
MY_ADDRESS = '1655+Nelson+Street+Vancouver+Canada'


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

if __name__ == "__main__": 
    main()