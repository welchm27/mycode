#!/usr/bin/env python3

def main():

    #check hostname against expected value
    ## collect input from user
    hostname = input("What value should we set for hostname?")

    ## here we use the str.lower() method to return a lowercase string
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    ## always print out to the user
    print("Exiting the script")

if __name__ == "__main__":
    main()
