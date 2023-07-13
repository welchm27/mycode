#!/usr/bin/env python3

def main():
    ## create file object in "r"ead mode
    with open("vlanconfig.cfg", "r") as configfile:
        ## readlines() creates a list by reading target
        ## file line by line
        configlist = configfile.readlines()

    ## file was just auto closed

    ## each item of the list now has the "\n" characters back
    print(configlist)


if __name__ == "__main__":
    main()
