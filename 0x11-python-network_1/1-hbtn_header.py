#!/usr/bin/python3
"""sends a request to a URL argument and displays the value of the
    X-Request-Id variable in the response header"""
import urllib.request
import sys


if __name__ = "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
