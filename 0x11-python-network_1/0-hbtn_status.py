#!/usr/bin/python3

import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
output = '''    - type: {}
    - content: {}
    - utf8 content: {}'''
with urllib.request.urlopen(req) as response:
    the_content = response.read()
    the_type = type(the_content)
    the_utf8 = the_content.decode('utf-8')
    print(output.format(the_type, the_content, the_utf8))
