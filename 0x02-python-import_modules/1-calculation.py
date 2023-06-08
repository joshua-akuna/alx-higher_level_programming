#!/usr/bin/python3
res = __import__('calculator_1')

a = 10
b = 5

print("{:d} + {:d} = {:d}".format(a, b, res.add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, res.sub(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, res.mul(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, int(res.div(a, b))))
