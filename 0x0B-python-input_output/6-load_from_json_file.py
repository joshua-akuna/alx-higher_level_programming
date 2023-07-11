#!/usr/bin/python3
"""The module defines the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """The function creates an Object from a 'JSON file'"""
    with open(filename, 'r', encoding='UTF8') as f:
        return json.loads(f.read())
