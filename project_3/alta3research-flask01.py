#!/usr/bin/env python3
"""Demonstrating flask API use by creating and converting data to JSON
This Flask API will convert a dictionary to JSON data, and uses a flask session
There is a login that stores username data, and removes it on logout
For return, the data is returned whether logged in or not, but if logged in, you get an additional welcome message"""

from flask import Flask
from flask import session
from flask import url_for
from flask import escape
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template

app = Flask(__name__)
app.secret_key = "any random string"

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
    # check if "username" is present in the session
    if "username" in session:
        # return MonsterData as JSON with an additional session message
        return jsonify({"message": "Welcome, " + session["username"], "data": MonsterData})
    else:
        # returning MonsterData as JSON without the session welcome message
        return jsonify(MonsterData)

# Login route to set the "username" session data
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        return redirect('/')
    return "Invalid request method"

# Logout route to remove the "username" session data
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
