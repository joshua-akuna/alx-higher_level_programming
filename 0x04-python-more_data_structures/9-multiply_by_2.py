#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_map = {}
    for key in a_dictionary.keys():
        new_map[key] = a_dictionary[key] * 2
    return (new_map)
