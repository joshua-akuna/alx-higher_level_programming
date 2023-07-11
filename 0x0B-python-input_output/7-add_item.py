#!/usr/bin/python3
"""The module contains functionalities that adds all arguments
to a Python list, and then save them to a file
"""

# imports the required modules
import json
from sys import argv
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

# the file to save and load the list from
filename = 'add_item.json'

try:
    _list = load_from_json(filename)
except (ValueError, FileNotFoundError):
    _list = []

_list.extend(argv[1:])
save_to_json(_list, filename)
