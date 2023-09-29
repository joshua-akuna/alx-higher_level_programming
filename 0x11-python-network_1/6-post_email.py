#!/usr/bin/python3
"""The script sends a post request to a URL argument with a body
    of an email argument and diplays the response body
"""
import requests
import sys


if __name__ == '__main__':
    res = requests.post(sys.argv[1], {"email" : sys.argv[2]})
    print(res.text)
