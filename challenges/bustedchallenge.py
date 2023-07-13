#!/usr/bin/env python3

def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True:
        name= input("What is your name?\n>")
        num= int(input("Pick a number between 1 and 3: "))

        if name and num in words.keys():
            # if the var name has a vlue
            # if num is one of the above options
            # Hi <name>! Welcome to Day 2 of Python Training!
            print("Hi " + name.capitalize() + "! Have a " + words[num] + " day!")
            break
        else:
          print("Come on, follow directions. Try again.")
          continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!

if __name__ == "__main__":
    main()
