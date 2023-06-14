#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_map = a_dictionary.copy()
    for key in new_map.keys():
        new_map[key] = new_map[key] * 2
    return (new_map)
