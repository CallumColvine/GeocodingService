# GeocodingService
##Small program designed to retrieve lat and long values based on an address.

This program can be run locally through the command line, or called as a RESTful API when running as a server.

Requirements:
Python 3.6 (for using json.loads() to unpack bytes data types)

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
```

##To Run:

Running locally via the command line:
```
python3.6 main.py --address="1655 Nelson Street, Vancouver, Canada" --mode="firstResult"
```

Running to be callable as a RESTful API
```
python3.6 main.py --server
curl --get 0.0.0.0:8000 --data-urlencode "address=1655 Nelson Street, Vancouver, Canada"
```
The RESTful API will:
Return 200 and the lat/lon values found for requests with existing lat/lon values.
Return 404 for requests with non-existant lat/lon values
