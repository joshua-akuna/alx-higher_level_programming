#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    res = 0
    iflag = False
    xflag = False
    cflag = False
    for index, val in enumerate(roman_string):
        if val == "M":
            res += 1000
            if cflag:
                res -= 200
                cflag = False
        if val == "D":
            res += 500
            if cflag:
                res -= 200
                cflag = False
        if val == "C":
            if xflag:
                res += 100 - 20
                xflag = False
            else:
                res += 100
                cflag = True
        if val == "L":
            if xflag:
                res += 50 - 20
                xflag = False
            else:
                res += 50
        if val == "X":
            if iflag:
                res += 10 - 2
                iflag = False
            else:
                res += 10
                xflag = True
        if val == "V":
            res += 5
            if iflag:
                res -= 2
                iflag = False
        if val == "I":
            res += 1
            iflag = True

    return (res)
