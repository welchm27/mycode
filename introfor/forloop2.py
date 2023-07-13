#!/usr/bin/env python3

def main():

    vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
    # create a second list of strings
    approved_vendors = ["cisco", "juniper", "big_ip"]
    # loop across the list called vendors
    for x in vendors:
        print("\nThe vendor is " + x, end="")   # newline, print current vendor
        if x not in approved_vendors:   # if x does not appear in the approved vendors list
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended")  # print when loop finishes

if __name__ == "__main__":
    main()
