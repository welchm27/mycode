#!/usr/bin/env python3

def main():

    ## prompt for user input
    ipchk = input("Apply an IP address: ")

    # if user set IP of gateway
    if ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
    elif ipchk:  # if any data is provided, this will test true
        print("Looks liek the IP address was set: " + ipchk)
    else:
        print("You did not provide an input.")


if __name__ == "__main__":
    main()
