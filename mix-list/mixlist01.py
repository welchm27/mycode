#!/usr/bin/env python3

def main():
    ## create a list containing three items
    my_list = ["192.168.0.5", 5060, "UP"]

    ## return the IP address from the list
    print("The first item in the list (IP): " + my_list[0])

    ## return the port
    print("The second item in the list (port): " + str(my_list[1]))

    ## return the last item in teh list
    print("The last item in teh list (state): " + my_list[2])



main()
