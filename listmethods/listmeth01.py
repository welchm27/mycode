#!/usr/bin/env python3

def main():
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    print(proto)
    proto.append("dns") # this line will add "dns" to the end of the list
    protoa.append("dns") # this line will add "dns" to the end of our list
    print(proto)
    proto2 = [22, 80, 443, 53] # a list of common ports
    proto.extend(proto2) #pass proto 2 as an arg to the extend method
    print(proto)
    protoa.append(proto2) # pass proto2 as an arg to the append method
    print(protoa)
    proto.insert(2, "vpn")  # add "vpn" to position 2 of the list
    print(proto)
    protoa.insert(2, "vpn")  # add "vpn" to position 2 of the list
    print(protoa)

if __name__ == "__main__":
    main()
