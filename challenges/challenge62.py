#!/usr/bin/env python3

def main():

    farms = [
         {
             "name": "NE Farm", 
             "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
             },
         {
             "name": "W Farm", 
             "agriculture": ["pigs", "chickens", "llamas"]
             },
         {
             "name": "SE Farm", 
             "agriculture": ["chickens", "carrots", "celery"]
             }]
    not_animals = ["carrots", "celery"]

    # iterate through NE Farm to return all the animals
    for animal in farms[0]["agriculture"]:
        print(animal)

    # allow the user to choose chich farm to return agriculture from
    for farm in farms:
        print("-", farm["name"])
    choice = input("Pick a farm!\n")
    # return all agriculture from the chosen farm
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            print(farm["agriculture"])
    
    # create a second input for only animals to be returned
    for farm in farms:
        print("-", farm["name"])
    choice = input("Pick a farm to see only animals!\n")
    # return only if on the animals list above
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for ag_item in farm["agriculture"]:
                if ag_item not in not_animals:
                    print(ag_item)


    


if __name__ == "__main__":
    main()
