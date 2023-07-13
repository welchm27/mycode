#!/usr/bin/env python3

def main():
    # set variable bottles to an int of what the user puts
    bottles = int(input("How many bottles do you want to start at? "))
    # repeating line so setting it as a variable
    line1 = " bottles of beer on the wall! "
    # don't let the user count higher than 100
    while bottles > 100:
        bottles = int(input("You may only go up to 100 bottles.  How many would you like to start at?"))
    # loop through the max bottles 
    for i in range(bottles, 0, -1):
        print(str(i) + line1)
        print(str(i) + line1 + str(i) + " bottles of beer! You take one down, pass it around!")


if __name__ == "__main__":
    main()
