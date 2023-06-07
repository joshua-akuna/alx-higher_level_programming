#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        return ((10 - (number % 10)) % 10 * -1)
    else:
        return (number % 10)

print(print_last_digit(print_last_digit(67)))
print(print_last_digit(print_last_digit(998)))
print(print_last_digit(print_last_digit(-67478)))
print(print_last_digit(print_last_digit(0)))
