#!/usr/bin/python3
"""The script sends a request to the URL argument and displays the value
    of the 'X-Request-Id' header variabl
"""
import sys
import requests


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
