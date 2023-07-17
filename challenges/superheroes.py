classinfo = {
    "all": [
        {
            "name": "Ariana",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Lily",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Eric",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Exxon",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Jason",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "James",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Helicopter Propulsion",
        },
        {
            "name": "Kevin",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Michael",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Immobility",
        },
        {
            "name": "Raylan",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Immutability",
        },
        {
            "name": "Richard",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Joseph",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Jet Propulsion",
        },
        {
            "name": "Josia",
            "skill level": "fine",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Kendra",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Mobile Invulnerability",
        },
        {
            "name": "Tito",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Muscle Manipulation",
        },
        {
            "name": "Ryan",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Nail Manipulation",
        },
        {
            "name": "Sabin",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Sheraz",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Sonic Voice",
        },
        {
            "name": "Sunny",
            "skill level": "remarkable",
            "spirit animal": "Alpaca",
            "super power": "Hydrokinesis",
        },
    ]
}

all_students = classinfo["all"]
# print(all_students)
for student in all_students:
    if student["name"] == "Michael":
        myName = student["name"]
        myAnimal = student["spirit animal"]
        mySkill = student["skill level"]
        myPower = student["super power"]
# print(myName)



print(f"My name is {myName} and my spirit animal is {myAnimal}.")
print(f"My name is {myName} and my skills are {mySkill}.")
print(f"My name is {myName} and my super power is {myPower}.\n")


for student in all_students:
    studentName = student["name"]
    studentAnimal = student["spirit animal"]
    studentSkill = student["skill level"]
    studentPower = student["super power"]
    print(f"{studentName}, a {studentSkill} {studentAnimal} of a programmer, possesses a {studentPower} factor for moonlighting as a superhero!")
# print(myName)