#!/usr/bin/env python3

import requests
import shutil  # to save the image locally
import wget


def main():
    pokenum = input("Pick a number between 1 and 151!\n")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # print(pokeapi)

    ## part 1:
    frontDef = pokeapi["sprites"]["front_default"]
    print(frontDef)

    ## part 2:
    #print(pokeapi["moves"])
    #for x in pokeapi["moves"]:
    #    print(x["move"]["name"])
    
    ## part 3:
    games = pokeapi["game_indices"]
    count = 0
    
    for game in games:
        count += 1
    print(f"This pokemon appeared in {count} games!")

    ## this can be done without a for loop by:
    ## use the len() function on pokeapi["game_indices"]

    ## BONUSES!
    wget.download(frontDef, "/home/student/static/")


if __name__ == "__main__":
    main()
