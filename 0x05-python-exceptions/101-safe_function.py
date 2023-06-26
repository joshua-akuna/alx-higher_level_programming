#!/usr/python3

import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(args[0], args[1])
    except BaseException as be:
        print("Exception: {}".format(be), file=sys.stderr)
        return None
    return (res)
