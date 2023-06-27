#!/usr/bin/python3

class Square:
    """Defines the constructor for the Square class the initializes
        the private instance size and position tuple of the instance(self)"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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
        return (self.__position)

    """Defines the setter for the private instance position property"""
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    """The area method returns the area = size * size of the
        a Square instance"""
    def area(self):
        return (self.__size * self.__size)

    """prints a square of '#' of length size"""
    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("_" * self.__position[0], end='')
            for j in range(self.__size):
                print("{}".format('#'), end='')
            print()
