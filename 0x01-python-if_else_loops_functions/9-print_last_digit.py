#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        return ((10 - (number % 10)) % 10 * -1)
    else:
        return (number % 10)
