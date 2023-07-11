#!/usr/bin/python3
"""The module defines the read_file function"""


def read_file(filename=""):
    """Reads a text file(UTF-8) and prints to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
