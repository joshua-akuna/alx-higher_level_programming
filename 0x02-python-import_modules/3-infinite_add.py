#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    for item in sys.argv[1:]:
        sum = sum + int(item)
    print(sum)
