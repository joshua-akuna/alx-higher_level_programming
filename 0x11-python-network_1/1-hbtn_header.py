#!/usr/bin/python3
"""
    sends a request to a URL argument and displays the value of the
    X-Request-Id variable in the response header
"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as res:
    print(res.headers.get("X-Request-Id"))
