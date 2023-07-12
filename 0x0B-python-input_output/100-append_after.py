#!/usr/bin/python3
"""The module contains the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string
    """
    with open(filename, "r+") as f:
        search_string = ""
        text = ""
        for line in f:
            if search_string in line:
                line += new_string
            text += line
        f.seek(0)
        f.write(text)
