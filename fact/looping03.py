#!/usr/bin/env python3

# standard library import
# allows us to generate UUIDs
import uuid

def main():
    howmany = int(input("How many UUIDs should be generated? "))

    print("Generating UUIDs...")

    # range is required because an int cannot be looped
    for rando in range(howmany):
        print(uuid.uuid4())   # each time through the loop produces an UUID


if __name__ == "__main__":
    main()
