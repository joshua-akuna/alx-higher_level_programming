#!/usr/bin/python3
"""The script fetches a URL response
"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - body: {}".format(body))
    print("    - utf8 content: {}".format(body.decode('utf-8')))
