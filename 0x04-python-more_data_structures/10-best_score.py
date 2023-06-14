#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    res = ""
    maxim = -100000
    for key, val in a_dictionary.items():
        if val > maxim:
            res = key
            maxim = val
    return res;
