#!/usr/bin/python3
"""The module contains the from_json_string function"""
import json


def from_json_string(my_str):
    """The function returns an object (Python data structure)
    representation of a json string
    """
    return json.loads(my_str)
