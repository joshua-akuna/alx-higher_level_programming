#!/usr/bin/python3
def fizzBuzz():
    for num in range(1, 101):
        s = ''
        if num % 3 == 0 and num % 5 == 0:
            s = 'FizzBuzz'
        elif num % 3 == 0:
            s = 'Fizz'
        elif num % 5 == 0:
            s = 'Buzz'
        else:
            s = str(num)
        print("{}".format(s), end=' ')
    print()

fizzBuzz()
