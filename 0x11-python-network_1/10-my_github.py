#!/usr/bin/python3

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 3:
        auth = {"username": sys.argv[1], "password": sys.argv[2]}
        res = requests.get(f"https://api.github.com/users/{sys.argv[1]}", auth)
        print(res.json().get('id'))
