#!/usr/bin/python3
"""The script sends a POST request to a 'http://0.0.0.0:5000/search_user'
with a request parameter q and displays
    - a json response if response is a valid json
    - "Not a valid json" if json response is invalid
    - "No result" if json response is empty
"""
import sys
import requests
import json


if __name__ == '__main__':
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        dict_response = res.json()
        if dict_response:
            print('[{}] {}'.format(
                dict_response.get('id'), dict_response.get('name')))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
