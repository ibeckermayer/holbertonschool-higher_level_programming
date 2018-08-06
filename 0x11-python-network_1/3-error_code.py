#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
