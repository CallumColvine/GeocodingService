import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

'''
GenericGeocoder is used as an interface for the Google/Here geocoders
'''
class GenericGeocoder(object):
    def __init__(self, unformattedAddress):
        self.unformattedAddress = unformattedAddress
        self.formattedAddress = ""
        self.url = ""
        self.urlBase = ""
        self.lat = 0
        self.lon = 0

    def formatAddress(self):
        # Spaces -> '+'
        # Commas -> '%2C'
        logging.debug("Inputted address is: {}".format(self.unformattedAddress))
        self.formattedAddress = self.unformattedAddress.replace(" ", "+")
        self.formattedAddress = self.formattedAddress.replace(",", "%2C")
        logging.debug("Formatted address is: {}".format(self.formattedAddress))

    def formatRequest(self):
        return None

    def getLatLon(self):
        return None
