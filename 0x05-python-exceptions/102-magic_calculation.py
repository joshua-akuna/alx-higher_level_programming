#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for item in range(1, 3):
        try:
            if item <= a:
                result += (a ** b) / item
            else:
                raise Exception('Too far')
        except Exception:
            result = b + a
            break
    return (result)
