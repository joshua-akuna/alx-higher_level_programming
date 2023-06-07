#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    mod = (10 - (number % 10)) % 10 * -1
else:
    mod = number % 10

if mod > 5:
    str = 'and is greater than 5'
elif mod == 0:
    str = 'and is 0'
else:
    str = 'and is less than 6 and not 0'

print(f'Last digit of {number} is {mod} {str}')
