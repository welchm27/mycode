#!/usr/bin/env python3

import requests
import pprint

#TODO demonstrate proficiency with the requests HTTP library
#TODO send a GET request to the flask01 API (it should target the endpoint that returns JSON)
#TODO Take the returned JSON and "normalize" it into a format that is easy for users to understand

URL= "http://127.0.0.1:2224/"

resp= requests.get(URL).json()

pprint(resp)