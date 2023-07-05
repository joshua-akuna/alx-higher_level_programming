#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

if __name__ == '__main__':
    my_square = Rectangle.square(5)
    fmt = "Area: {} - Perimeter: {}"
    print(fmt.format(my_square.area(), my_square.perimeter()))
    print(my_square)
