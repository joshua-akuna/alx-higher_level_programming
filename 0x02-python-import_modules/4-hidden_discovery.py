#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    mod = dir(hidden_4)
    for name in mod:
        if name.startswith('__'):
            continue
        print('{:s}'.format(name))
