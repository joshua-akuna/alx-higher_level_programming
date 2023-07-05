#!/usr/bin/python3
""" This module defines the text_indentation function """


def text_indentation(text):
    """
    Function prints a text with 2 new lines after each of these
    charaters: .?: found in the text argument with no spaces at
    the beginning and end of each printed line.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    spec = '.?:'
    new_text = "".join([ch if ch not in spec else ch + "\n\n" for ch in text])
    new_text = "\n".join([line.strip() for line in new_text.split("\n")])
    print(new_text, end="")
