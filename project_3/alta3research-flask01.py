#!/usr/bin/env python3
"""Demonstrating flask API use by creating and converting data to JSON"""

from flask import Flask
from flask import session
from flask import url_for
from flask import escape
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template


#TODO: create at least two endpoints
#TODO: One endpoint should return JSON
#TODO: One additional feature from the following list:
"""one endpoint returns HTML that uses jinja2 logic
requires a session value be present in order to get a response
writes to/reads from a cookie
reads from/writes to a sqlite3 database"""

app = Flask(__name__)


# Monster Data 
MonsterData = {
    "name": "Drow",
    "meta": "Medium humanoid, neutral evil",
    "Armor Class": "15 (Chain Shirt)",
    "Hit Points": "13 (3d8)",
    "STR": "10",
    "DEX": "14",
    "CON": "10",
    "INT": "11",
    "WIS": "11",
    "CHA": "12", 
    "img_url": "https://media-waterdeep.cursecdn.com/avatars/thumbnails/16/501/1000/1000/636376310726273495.jpeg"
}

# if the user hits the root of our API
@app.route('/')
def index():
    # returning MonsterData as JSON
    return jsonify(MonsterData)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
