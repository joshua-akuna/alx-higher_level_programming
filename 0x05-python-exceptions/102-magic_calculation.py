#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for item in range(1, 3):
        try:
            if item > a:
                raise Exception('Too far')
            else:
                res += (a ** b) / i
        except BaseException:
            result (a + b)
            break
    return (res)
