#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b < 0:
        for i in range(b, 0):
            res = res * 1/a
    elif b > 0:
        for i in range(0, b):
            res = res * a
    else:
        res = a
    return (res)
