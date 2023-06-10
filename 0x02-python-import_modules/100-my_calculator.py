#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

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
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, res))
    exit(0)
