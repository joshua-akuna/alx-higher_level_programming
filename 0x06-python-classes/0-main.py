#!/usr/bin/python3
"""imports the Square class from
    the 0-square.py file"""
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
