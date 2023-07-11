#!/usr/bin/python3
"""The module contains the append_write function"""


def append_write(filename="", text=""):
    """The function appends a string at the end of a text(UTF*) and
    returns the number of characters added
    """
    with open(filename, 'a', encoding='UTF*') as f:
        return f.write(text)
