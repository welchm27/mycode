#!/usr/bin/env python3

def main():
    # open file in read mode
    dnsfile = open("dnsservers.txt", "r")

    # create list of lines of text
    dnslist = dnsfile.readlines()

    # loop over lines
    for svr in dnslist:
        # print and end without a new line
        print(svr, end="")  # the line we read ALREADY contains a \n (newline)

    # close the file (we created the list of lines)
    dnsfile.close()  # best practice to close your file


if __name__ == "__main__":
    main()
