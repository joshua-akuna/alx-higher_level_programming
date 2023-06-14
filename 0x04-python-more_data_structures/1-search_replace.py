#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for key, val in enumerate(new_list):
        if val == search:
            new_list[key] = replace
    return new_list
