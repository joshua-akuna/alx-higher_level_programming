#!/usr/bin/python3
"""The module contains the to_json_string function"""

import json


def to_json_string(my_obj):
    """The function the JSON representation of an object"""
    return json.dumps(my_obj)
