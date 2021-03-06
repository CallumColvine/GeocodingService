from generic_geocoder import GenericGeocoder
import json
import urllib.parse
import urllib.request


# Retrieved from https://developers.google.com/maps/documentation/geocoding/start
GOOGLE_API_KEY = "AIzaSyA-YjJR_ILnJurVXGpO2Rtk6ToE6P02djs"
GOOGLE_URL_BASE = "https://maps.googleapis.com/maps/api/geocode/json?"


class GoogleGeocoder(GenericGeocoder):
    def __init__(self, unformattedAddress):
        super(GoogleGeocoder, self).__init__(unformattedAddress)

    def formatRequest(self):
        self.url = GOOGLE_URL_BASE + "address=" + self.formattedAddress + "&key=" \
                + GOOGLE_API_KEY

    def getLatLon(self):
        request = urllib.request.Request(self.url)
        with urllib.request.urlopen(request) as response:
            page = response.read()
            page = json.loads(page)
            location = page.get("results", {})
            if len(location) > 0:
                location = location[0].get("geometry", {}).get("location")
                self.lat = location.get("lat")
                self.lon = location.get("lng")
