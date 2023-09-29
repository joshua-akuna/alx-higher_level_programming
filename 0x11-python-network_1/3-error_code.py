#!/usr/bin/python3
"""
The script sends a request to a URL and displays its response body
decode in utf-8
    - urllib.error.HTTPError exceptions must be managed
"""

import sys
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.status))
