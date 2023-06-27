#!/usr/bin/python3
"""imports the math module"""
import math

"""The definition for the MagicClass class"""


class MagicClass:
    """A constructor for the MagicClass class that initializes the
        radius property"""
    def __init__(self, radius=0):
        self.__radius = 0
        if (not isinstance(radius, int) and not isinstance(radius, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    """The funtion returns the area of the MagicClass instance"""
    def area(self):
        return math.pi * self.__radius * self.__radius

    """The funtion returns the circumference of the MagicClass instance"""
    def circumference(self):
        return 2 * math.pi * self.__radius
