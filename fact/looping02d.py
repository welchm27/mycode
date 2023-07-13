#!/usr/bin/env python3

def main():
    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:  # 'r' is read mode
        # indent to keep the dnsfile object open
        # loop across the lines in the file
        for svr in dnsfile:
            svr = svr.rstrip('\n')  # remove newline char if it exists
                                    # would exist on all but the last line
            # IF the string svr ends with 'org'
            if svr.endswith('org'):
                with open("org-domain.txt", "a") as srvfile:  # 'a' is append mode
                    srvfile.write(svr + "\n")
            # ELSE-IF the string svr ends with 'com'
            elif svr.endswith('com'):
                with open("com-domain.txt", "a") as srvfile:
                    srvfile.write(svr + "\n")
    # no need to close our file - closed automatically


if __name__ == "__main__":
    main()
