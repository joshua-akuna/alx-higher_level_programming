#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        mod = ((10 - (number % 10)) % 10)
    else:
        mod = (number % 10)
    print("{}".format(mod), end='')
    return abs(mod)
