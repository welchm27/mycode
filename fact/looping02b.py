#!/usr/bin/env python3

def main():

    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:
        # indent to keep the dnsfile object open
        # create list of lines
        dnslist = dnsfile.readlines()
        # loop over lines
        for svr in dnslist:
            # print and end without a new line
            print(svr, end="")

    # no need to close our file - closed automatically

if __name__ == "__main__":
    main()
