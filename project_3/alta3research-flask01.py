#!/usr/bin/env python3
"""Demonstrating flask API use by creating and converting data to JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify


#TODO: create at least two endpoints
#TODO: One endpoint should return JSON
#TODO: One additional feature from the following list:
"""one endpoint returns HTML that uses jinja2 logic
requires a session value be present in order to get a response
writes to/reads from a cookie
reads from/writes to a sqlite3 database"""

app = Flask(__name__)

# Monster Data 
MonsterData = [{
    "name": "Drow",
    "meta": "Medium humanoid, neutral evil",
    "Armor Class": "15 (Chain Shirt)",
    "Hit Points": "13 (3d8)",
    "Speed": "30 ft. ",
    "STR": "10",
    "STR_mod": "(+0)",
    "DEX": "14",
    "DEX_mod": "(+2)",
    "CON": "10",
    "CON_mod": "(+0)",
    "INT": "11",
    "INT_mod": "(+0)",
    "WIS": "11",
    "WIS_mod": "(+0)",
    "CHA": "12",
    "CHA_mod": "(+1)",
    "Skills": "Perception +2, Stealth +4",
    "Senses": "Darkvision 120 ft.,  Passive Perception 12",
    "Languages": "Elvish, Undercommon",
    "Challenge": "1/4 (50 XP)",
    "Traits": "<p><em><strong>Fey Ancestry.</strong></em> The drow has advantage on saving throws against being charmed, and magic can’t put the drow to sleep.</p><p><em><strong>Innate Spellcasting.</strong></em> The drow’s spellcasting ability is Charisma (spell save DC 11). It can innately cast the following spells, requiring no material components:</p><p>At will: dancing lights</p><p>1/day each: darkness, faerie fire</p><p><em><strong>Sunlight Sensitivity.</strong></em> While in sunlight, the drow has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.</p>",
    "Actions": "<p><em><strong>Shortsword.</strong></em> <em>Melee Weapon Attack:</em> +4 to hit, reach 5 ft., one target. <em>Hit:</em> 5 (1d6 + 2) piercing damage.</p><p><em><strong>Hand Crossbow.</strong></em> <em>Ranged Weapon Attack:</em> +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target wakes up if it takes damage or if another creature takes an action to shake it awake.</p>",
    "img_url": "https://media-waterdeep.cursecdn.com/avatars/thumbnails/16/501/1000/1000/636376310726273495.jpeg"
  }]

@app.route('/')
def index():
    # jsonify returns legal JSON
    return jsonify(MonsterData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)