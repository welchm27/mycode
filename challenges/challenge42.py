#!/usr/bin/env python3

def main():
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    challenge_string= (f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")
    trial_string= (f"My {trial[2]['goggles']}! The {trial[2]['eyes']} do {trial[3]}!")
    nightmare_string= (f"My {nightmare[0]['user']['name']['first']}! The {nightmare[0]['kumquat']} do {nightmare[0]['d']}!")

    print(f{challenge_string}\n{trial_string}\n{nightmare_string})


if __name__ == "__main__":
    main()
