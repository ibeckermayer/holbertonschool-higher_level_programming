#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
