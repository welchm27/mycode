#!/usr/bin/env python3

def main():

    # create the list called vendors
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
    # loop across the list vendors
    for x in vendors:
        print("The vendor is: " + x)
    print("\nOur loop has ended.")

if __name__ == "__main__":
    main()
