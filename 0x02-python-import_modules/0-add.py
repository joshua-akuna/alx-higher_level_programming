#!/usr/bin/python3
res = __import__('add_0')

a = 1
b = 2
print('{:d} + {:d} = {:d}'.format(a, b, res.add(a, b)))
