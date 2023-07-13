#!/usr/bin/env python3

from subprocess import call

def main():
    # call() will issue ip link show up, which reveals those interfaces that are currently up
    call(["ip", "link", "show", "up"])
    print("This program will check your interfaces.")

    # prompt user for which interface they'd like more detail on
    interface = input("Enter an interface, like, ens3: ")

    # use the interface to issue ip addre show dev and reveal IPv4 and IPv6 details
    call(["ip", "addr", "show", "dev", interface])

    # use input collected to issue ip route show dev and reveal IPv4 and IPv6 details
    call(["ip", "route", "show", "dev", interface])


if __name__ == "__main__":
    main()
