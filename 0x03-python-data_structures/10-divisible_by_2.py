#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    res = list(map(lambda num: num % 2 == 0, new_list))
    return (res)
