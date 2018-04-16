from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json
from geocoder_handler import Geocoder

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class RestHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        geocoder = Geocoder()
        geocoder.address = self.getRequestAddress()
        logging.info("Set outgoing request address to {}".format(geocoder.address))
        geocoder.callHereGeocode(formatAddress=False)
        geocoder.callGoogleGeocode(formatAddress=False)
        position = geocoder.compareAndPickResults()
        if position is not None and (position[0] != 0 and position[1] != 0):
            print ("Latitude is:  ", position[0])
            print ("Longitude is: ", position[1])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({'latitude': position[0]}).encode())
        self.wfile.write(json.dumps({'longitude': position[1]}).encode())
        return

    def getRequestAddress(self):
        address = self.requestline.split("?")[1]
        address = address.split(" ")[0]
        address = address.split("=")[1]
        return address

    # def parseAddressFromRequestLine(self):
    #     address = address.replace()
    #     return address

httpd = HTTPServer(('0.0.0.0', 8000), RestHTTPRequestHandler)

def serverLoop():
    while True:
        httpd.handle_request()