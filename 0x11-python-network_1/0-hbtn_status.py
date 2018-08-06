#!/usr/bin/python3

import urllib.request

req = urllib.request.Request("https://intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    the_content = response.read()
    the_type = type(the_content)
    the_utf8 = the_content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(the_type))
    print("\t- content: {}".format(the_content))
    print("\t- utf8 content: {}".format(the_utf8))
