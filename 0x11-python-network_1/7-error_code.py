#!/usr/bin/python3
"""The script sends a request to a URL argument and displays the
    response body.
    - If response status code is less than or equals 400, print
        'Error code: <status code>'
"""
import sys
import requests


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)
