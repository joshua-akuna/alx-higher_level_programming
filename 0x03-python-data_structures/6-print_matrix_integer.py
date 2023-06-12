#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for item in row:
                if item == row[0]:
                    print("{:d}".format(item), end="")
                else:
                    print(" {:d}".format(item), end="")
            print()
    else:
        print()
