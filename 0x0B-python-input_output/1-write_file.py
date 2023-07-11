#!/usr/bin/python3
"""The module contains the write_file function"""


def write_file(filename="", text=""):
    """The function writes a string to a text file(UTF*) and
    returns the number of characters written
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
