from geocoder_handler import GeocoderHandler
from request_server import serverLoop
import logging


def main():
    logging.info("Geocoder program started")
    geocoder = GeocoderHandler()
    geocoder.parseArgs()
    # Starts up the RestHTTPRequestHandler infinite loop to listen for API calls
    if geocoder.runAsServer:
        serverLoop()
        exit()
    geocoder.callHereGeocode()
    geocoder.callGoogleGeocode()
    position = geocoder.compareAndPickResults()
    if position is not None and (position[0] != 0 and position[1] != 1):
        print ("Latitude is:  ", position[0])
        print ("Longitude is: ", position[1])
    else:
        print ("No latitude or longitude were found for the input address")

if __name__ == "__main__":
    main()
