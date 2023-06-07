#!/usr/bin/python3
for ten in range(10):
    for unit in range(ten + 1, 10):
        print("{:02d}".format(ten), "{:02d}".format(unit), sep=" ,", end=" , " if unit != 9 else "\n")
