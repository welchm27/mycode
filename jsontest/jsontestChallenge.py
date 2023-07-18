#!/usr/bin/env python3

import requests

# define the URLs we want to use
POSTURL = "http://validate.jsontest.com/"
IPURL = "http://ip.jsontest.com/"
TIMEURL = "http://time.jsontest.com"

def main():
    ## pull timestamp of now (TIMEURL)
    timeResp = requests.get(TIMEURL)
    # strip off JSON response and convert to PYTHONIC Data
    timeRespJson = timeResp.json()
    # display our PYTHONIC data
    print(timeRespJson['time'])
    timeResp = timeRespJson['time']

    ## pull IP address of current system (IPURL)
    # use requests library to send a GET request
    ipResp = requests.get(IPURL)
    # strip off JSON response and convert to PYTHONIC Data
    ipRespJson = ipResp.json()
    # display our PYTHONIC data
    print(ipRespJson['ip'])
    ipResp = ipRespJson['ip']

    ## read in a list of servers from a file called myservers.txt (will need to make)
    # read lines from myservers.txt
    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    ## format as {"json": "time: <<PART A>>, ip: <<PART B>>, mysvrs: [ <<PART C>> ]"}
    jsonToTest = {}
    jsonToTest["time"] = timeResp
    jsonToTest["ip"] = ipResp
    jsonToTest["mysvrs"] = mysvrs
    
    mydata = {}
    mydata["json"] = str(jsonToTest)

    ## validate your JSON with a POST
    resp = requests.post(POSTURL, data=mydata)

    # display PYTHONIC data (LIST / DICT)
    #print(respjson)
    respJson = resp.json()

    # display if the post is valid
    print(f"Is your JSON valid? {respJson['validate']}")


if __name__ == "__main__":
    main()
