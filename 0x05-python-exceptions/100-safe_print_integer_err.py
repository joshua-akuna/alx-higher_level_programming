#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    fmt = "Exception: Unknown format code 'd' for object of type '{}'"
    try:
        print("{:d}".format(value))
    except BaseException as be:
        print("Exception: {}".format(be), file=sys.stderr)
        return (False)
    return (True)
