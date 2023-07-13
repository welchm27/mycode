#!/usr/bin/env python3

def main():

    ## create file object in "r"ead mode
    configfile = open("vlanconfig.cfg", "r")

    ## display file to the screen - .read()
    print(configfile.read())

    # the "cursor" is now at the end of the file
    # we COULD close the file and reopen it to
    # move the cursor back to the top of the file

    ## close file
    #configfile.close()
    ## re-create file object to explore new method
    #configfile = open("vlanconfig.cfg", "r")

    # alternatively we can use the method `.seek`
    # this will move the cursor back to position 0,0
    # or the start of the file
    configfile.seek(0, 0)

    ########## EXPLORE READLINES ##########
    ## make a list of file lines - .readlines()
    configlist = configfile.readlines()
    print(configlist)

    ## Iterate through configlist
    for x in configlist:
       # print(x, end="")    # by default, print() ends in a new line
                            # by passing end="" print will not add a second
                            # new line character
        print(x.strip())    # by default, .strip will remove any whitespace or newlines
                            # therefore we no longer want to change "end=" from its default setting of
                            # a new line character

    ## Always close your file
    configfile.close()


if __name__ == "__main__":
    main()
