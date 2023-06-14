#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        val = a_dictionary[key]

        if isinstance(val, list):
            val_str = "[" + ", ".join(map(str, val)) + "]"
        else:
            val_str = str(val)
        print("{}: {}".format(key, val_str))
