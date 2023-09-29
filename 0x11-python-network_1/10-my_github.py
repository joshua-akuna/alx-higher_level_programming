#!/usr/bin/python3
"""The scripts takes github credentials as arguments and uses the
    GITHUB API to display the ID of the authenticated user
"""

import sys
import requests


if __name__ == '__main__':
    auth = {"username": sys.argv[1], "password": sys.argv[2]}
    res = requests.get(f"https://api.github.com/users/{sys.argv[1]}", auth)
    print(res.json().get('id'))
