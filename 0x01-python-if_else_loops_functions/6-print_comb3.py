#!/usr/bin/python3
for ten in range(0, 10):
    for unit in range(ten + 1, 10):
        if ten == 8 and unit == 9:
            print(89)
        else:
            print('{}{}, '.format(ten, unit), end='')
