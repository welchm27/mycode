#!/usr/bin/env python3

def main():
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n").lower()
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n").lower()

    marvelchars= {
    "starlord":
        {"real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

    "mystique":
        {"real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

    "hulk":
        {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
                }

    if char_name in marvelchars:
        if char_stat in marvelchars[char_name]:
            char_value = marvelchars[char_name][char_stat]
            if char_stat == "real name":
                char_value = char_value.title() # capitalize if "real name"
            print(f"{char_name.title()}'s {char_stat} is: {char_value}")
            
        else:
            print(f"{char_name} does not have a {char_stat} statistic.")
    else:
        print(f"{char_name} is not a valid character.")

    

if __name__ == "__main__":
    main()
