#!/usr/bin/env python3

def main():
    ## prompt the user for an input
    ipchk = input("Apply an IP address: ")

    # a provided string will test tru
    if ipchk:
        print("Looks like the IP address was set: " + ipchk)
    else:
        print("You did not provide an input.")


if __name__ == "__main__":
    main()
