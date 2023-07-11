#!/usr/bin/python3
"""The module contains the Student class"""


class Student:
    """A class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """A constructor that initializes the first_name,
        last_name and age public instance variables.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
