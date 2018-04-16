from here_geocoder import HereGeocoder
from google_geocoder import GoogleGeocoder
import argparse
import sys
import json

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)



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
        self.mode = self.modeList[0]
        self.hereResults = None
        self.googleResults = None

    def callHereGeocode(self, formatAddress=True):
        hereGeocoder = HereGeocoder(self.address)
        if formatAddress:
            hereGeocoder.formatAddress()
        else:
            hereGeocoder.formattedAddress = self.address
        hereGeocoder.formatRequest()
        hereGeocoder.getLatLon()
        self.hereResults = [hereGeocoder.lat, hereGeocoder.lon]
        logging.info("Results from Here API lat: {} lon: {}"\
            .format(str(self.hereResults[0]), str(self.hereResults[1])))

    def callGoogleGeocode(self, formatAddress=False):
        googleGeocoder = GoogleGeocoder(self.address)
        if formatAddress:
            googleGeocoder.formatAddress()
        else:
            googleGeocoder.formattedAddress = self.address
        googleGeocoder.formatRequest()
        googleGeocoder.getLatLon()
        self.googleResults = [googleGeocoder.lat, googleGeocoder.lon]
        logging.info("Results from Google API lat: {} lon: {}"\
            .format(str(self.googleResults[0]), str(self.googleResults[1])))

    def compareAndPickResults(self):
        if self.mode == 'firstResult':
            if self.hereResults is not None:
                return self.hereResults
            elif self.googleResults is not None:
                return self.googleResults
            else:
                return None
        elif self.mode == 'bestMatch':
            # Concept mode. Would take ALL results from API returns from Here 
            # and Google and return the closest match
            pass


    def parseArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-s',
            '--server',
            help='Boolean parameter specifying if the program should be run as \
                    a server',
            action='store_true'
        )        
        parser.add_argument(
            '-a',
            '--address',
            help='The address to get latitude and longitude for',
            type=str
        )
        parser.add_argument(
            '-m',
            '--mode',
            help='The mode used for picking the result latitude and longitude',
            choices=self.modeList,
            default=self.modeList[0]
        )
        args = parser.parse_args()
        self.runAsServer = args.server
        print (self.runAsServer)
        self.address = args.address
        if (self.address is None or self.address == "") and not self.runAsServer:
            sys.exit("Please provide a valid address")
        self.mode = args.mode
        logging.info("Parsed address: {}".format(self.address))
        logging.info("Parsed mode: {}".format(self.mode))