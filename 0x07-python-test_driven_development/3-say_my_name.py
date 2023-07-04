#!/usr/bin/python3
""" This module contains the say_my_name function """


def say_my_name(first_name, last_name=""):
    """ The say_my_name function """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
