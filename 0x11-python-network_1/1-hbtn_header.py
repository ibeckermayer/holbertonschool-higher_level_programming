#!/usr/bin/python3
import urllib.request
import sys

req = urllib.request.Request("https://intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    the_header = response.info()
    print(the_header["X-Request-Id"])

