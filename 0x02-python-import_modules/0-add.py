#!/usr/bin/python3
if __name__ == "__main__":
    res = __import__('add_0')

    a = 1
    b = 2
    print('{:d} + {:d} = {:d}'.format(a, b, res.add(a, b)))
