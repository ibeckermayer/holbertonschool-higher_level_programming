#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        the_header = response.info()
        print(the_header["X-Request-Id"])
