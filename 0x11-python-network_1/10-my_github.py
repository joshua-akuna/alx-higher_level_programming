#!/usr/bin/python3
"""The scripts takes github credentials as arguments and uses the
    GITHUB API to display the ID of the authenticated user
"""

import sys
import requests


if __name__ == '__main__':
    auth = (sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get('id', None))
