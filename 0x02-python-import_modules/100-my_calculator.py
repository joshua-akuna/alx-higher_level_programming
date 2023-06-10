#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator == '+':
        res = a + b
    elif operator == '-':
        res = a - b
    elif operator == '*':
        res = a * b
    elif operator == '/':
        res = a / b
    else:
        print('Unknown operator. Available operators: +, -, *, /')
        sys.exit(1)

    print("{:d} {:s} {:d} = {}".format(a, operator, b, res))
    sys.exit(0)
