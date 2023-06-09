#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print("{:d} arguments.".format(argc - 1))
    elif argc == 2:
        print("{:d} argument:".format(argc - 1))
    elif argc > 2:
        print("{:d} arguments:".format(argc - 1))

    for index, item in enumerate(sys.argv):
        if index == 0:
            continue
        print("{}: {}".format(index, item))
