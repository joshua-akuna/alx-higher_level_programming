#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return (str)

    res = ''
    for index in range(len(str)):
        if index == n:
            continue
        res = res + str[index]
    return res
