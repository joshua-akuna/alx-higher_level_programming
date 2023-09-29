#!/usr/bin/python3
"""The script sends a POST request to a url with an email variable as
parameter and displays the response body decoded in utf-8
"""
import sys
from urllib.request import Request, urlopen
import urllib.parse

req_body = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
req = Request(sys.argv[1], req_body)
with urlopen(req) as response:
    print(response.read())
