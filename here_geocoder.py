from copy import deepcopy
from generic_geocoder import GenericGeocoder
import json
import logging
import urllib.parse
import urllib.request


# Retrieved from https://developer.here.com/projects
HERE_APP_ID = "T8Yh97KaSNVLi0pA2AXi"
HERE_APP_CODE = "n0J58c0YsvFtUaX99I7UCQ"
HERE_URL_BASE = "https://geocoder.cit.api.here.com/6.2/geocode.json?"

class HereGeocoder(GenericGeocoder):
    def __init__(self, unformattedAddress):
        super(HereGeocoder, self).__init__(unformattedAddress)

    def formatRequest(self):
        self.url = HERE_URL_BASE + "searchtext=" + self.formattedAddress + \
            "&app_id=" + HERE_APP_ID + "&app_code=" + HERE_APP_CODE
        logging.debug("Here URL is: {}".format(self.url))

    def getLatLon(self):
        request = urllib.request.Request(self.url)
        with urllib.request.urlopen(request) as response:
            page = response.read()
            page = json.loads(page)
            logging.debug("Here response: {}".format(page))
            view = page.get("Response", {}).get("View", [])
            if len(view) > 0:
                points = view[0].get('Result', [])
                if len(points) > 0:
                    points = points[0].get("Location", {}).get("NavigationPosition")
                    if len(points) > 0:
                        points = points[0]
                        self.lat = deepcopy(points.get("Latitude"))
                        self.lon = deepcopy(points.get("Longitude"))
