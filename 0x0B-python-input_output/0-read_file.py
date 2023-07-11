#!/usr/bin/python3
"""The module defines the read_file function"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())

    if f.closed is False:
        f.close()
