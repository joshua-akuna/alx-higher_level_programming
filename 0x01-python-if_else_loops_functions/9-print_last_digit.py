#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        print((10 - (number % 10)) % 10)
    else:
        print(number % 10)
