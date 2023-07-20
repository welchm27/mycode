#!/usr/bin/env python3

import requests
from pprint import pprint

"""
Connect to my flask API and return the JSON data and convert it to PYTHONIC data.
Returning monster name, AC, HP, but you can return all stats by just using (resp)
"""

# URL to connect to my flask api (must be running)
URL= "http://127.0.0.1:2224/"

# get request from the URL and converting data from JSON to PYTHONIC
resp= requests.get(URL).json()

# Stats that I want to display (out of "name", "meta", "Armor Class", "Hit Points", 
# "STR", "DEX", "CON", "INT", "WIS", "CHA", "img_url"
name = resp["name"]
ac = resp["Armor Class"]
hp = resp["Hit Points"]

## uncomment this out if you want to print all the monster stats
#pprint(resp)

# printing only the name, Armor Class and Hit Points (could use this in our game)
print(f"""
Monster Name: {name}
Monster Armor Class: {ac}
Monster Hit Points: {hp}""")
