#!/usr/bin/env python3

import requests
from pprint import pprint

#TODO demonstrate proficiency with the requests HTTP library
#TODO send a GET request to the flask01 API (it should target the endpoint that returns JSON)
#TODO Take the returned JSON and "normalize" it into a format that is easy for users to understand

URL= "http://127.0.0.1:2224/"

resp= requests.get(URL).json()

name = resp["name"]
ac = resp[0]["Armor Class"]
hp = resp[0]["Hit Points"]

#print(f"""Name: {name}
#Armor Class: {ac}
#Health Points: {hp}""")


pprint(resp)
#name=resp["monsters"]["name"]
#print(name)
