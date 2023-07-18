#!/usr/bin/env python3

import requests
import datetime
import reverse_geocoder as rg

URL = "http://api.open-notify.org/iss-now.json"

"""Returning the location of the ISS in latitude/longitude"""
def main():
    resp = requests.get(URL).json()
    
    ## initial print to confirm resp is being returned correctly
    #print(resp)

    lat = resp["iss_position"]["latitude"]
    lon = resp["iss_position"]["longitude"]
    epochTime = resp["timestamp"]
    dateTime = datetime.datetime.fromtimestamp(epochTime)
    coords_tuple = (lat, lon)

    result = rg.search(coords_tuple, verbose=False)
    geoName = result[0]["name"]
    geoCC = result[0]["cc"]

    print(f"Timestamp: {dateTime}")
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Lon: {lon}")
    print(f"Lat: {lat}")
    print(f"City/Country: {geoName}, {geoCC}")



if __name__ == "__main__":
    main()
