#!/usr/bin/python3
"""The module contains the Student class"""


class Student:
    """A class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """A constructor that initializes the first_name, last_name
        and age public instance variables.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}

    def reload_from_json(self, json):
        """replaces all attribute of the Student instances"""
        self.__dict__.update(json)
