#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
    print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter an IPV4 IP address:")

    ## the line below creates a single string that is passed to pring()
    # print ("You told me the IPV4 address is: " + user_input)

    ## print() can be given a series of objects separated by a comma
    print("You told me the IPV4 address is:", user_input)

    store_input = input("Please provide the vendor name associated to your device:")
    print("Your device vendor is: ", store_input)

main()
