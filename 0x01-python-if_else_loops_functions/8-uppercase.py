#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper_case = chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
        print("{}".format(upper_case), end='')
    print()
