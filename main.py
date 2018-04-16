from geocoder_handler import Geocoder
from request_server import serverLoop
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


def main():
    logging.info("Geocoder program started")
    geocoder = Geocoder()
    geocoder.parseArgs()
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
