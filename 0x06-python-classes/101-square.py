#!/usr/bin/python3
"""Definition for the Square class"""


class Square:
    """Defines the constructor for the Square class the initializes
        the private instance size and position tuple of the instance(self)"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """Defines the getter for the private instance self property"""
    @property
    def size(self):
        return (self.__size)

    """Defines the setter for the private instance self property"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Defines the getter for the private instance position property"""
    @property
    def position(self):
        return self.__position

    """Defines the setter for the private instance position property"""
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2\
                or type(value[0]) is not int or type(value[1]) is not int\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """The area method returns the area = size * size of the
        a Square instance"""
    def area(self):
        return (self.size * self.size)

    """returns a square of '#' of length size"""
    def __repr__(self):
        to_string = ''
        if self.__size == 0:
            return to_string

        to_string += '\n' * self.position[1]
        for item in range(self.size):
            if (item):
                to_string += '\n'
            to_string += " " * self.position[0]
            to_string += "#" * self.size
        return (to_string)

    """prints a square of '#' of length size"""
    def my_print(self):
        print(self, end="")
