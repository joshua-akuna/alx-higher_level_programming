#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    offset = 0
    if letter % 2 == 1:
        offset = 32
    print('{}'.format(chr(letter - offset)), end='')
