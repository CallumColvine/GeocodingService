import argparse
from here_geocoder import HereGeocoder
from google_geocoder import GoogleGeocoder

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


''' 
ToDo:
- Call Here geocoding services                          DONE
- Call Google geocoding stuff                           DONE
- Parse input arguments for command line interface      DONE
- Write picking method between Here and Google results  IN PROGRESS
- Enable RESTful calls on app                           TODO
'''

class Geocoder(object):
    '''
    inputAddress is a string including spaces
    mode specifies how the program should work
        - firstResult means use the first result from Here/Google as authority
        - bestMatch means use the address that both Here/Google come up with
        ...
    '''
    def __init__(self):
        self.modeList = ['firstResult', 'bestMatch'] 
        self.address = None
        self.mode = None
        self.hereResults = None
        self.googleResults = None

    def callHereGeocode(self):
        hereGeocoder = HereGeocoder(self.address)
        hereGeocoder.formatAddress()
        hereGeocoder.formatRequest()
        hereGeocoder.getLatLon()
        self.hereResults = [hereGeocoder.lat, hereGeocoder.lon]
        logging.info("Results from Here API lat: {} lon: {}"\
            .format(str(self.hereResults[0]), str(self.hereResults[1])))

    def callGoogleGeocode(self):
        googleGeocoder = GoogleGeocoder(self.address)
        googleGeocoder.formatAddress()
        googleGeocoder.formatRequest()
        googleGeocoder.getLatLon()
        self.googleResults = [googleGeocoder.lat, googleGeocoder.lon]
        logging.info("Results from Here API lat: {} lon: {}"\
            .format(str(self.googleResults[0]), str(self.googleResults[1])))

    def parseArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            '--address',
            help='The address to get latitude and longitude for',
            type=str,
            required=True
        )
        parser.add_argument(
            '-m',
            '--mode',
            help='The mode used for picking the result latitude and longitude',
            choices=self.modeList,
            default=self.modeList[0]
        )
        args = parser.parse_args()
        self.address = args.address
        if self.address is None or self.address == "":
            sys.exit("Please provide a valid address")
        self.mode = args.mode
        logging.info("Parsed address: {}".format(self.address))
        logging.info("Parsed mode: {}".format(self.mode))


def main():
    logging.info("Geocoder program started")
    geocoder = Geocoder()
    geocoder.parseArgs()
    # geocoder.callHereGeocode()
    geocoder.callGoogleGeocode()

if __name__ == "__main__": 
    main()
