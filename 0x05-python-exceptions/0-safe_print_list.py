#!/usr/bin/python3

def safe_print_list(arr, size):
    _size = 0
    try:
        for i in range(size):
            print(arr[i], end="")
            _size += 1
    except IndexError:
        pass
    print()
    return (_size)
