#!/usr/bin/python3
"""This module contains programs that solves the N queens puzzle"""
import sys


def is_queen_safe(board, row, col):
    """This function returns True if the queen will
        is safe in the current location on the board else False
    """
    # check if there's a queen in the current column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check if there's a queen in the in the
    # upper diagonal on the left side
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # checks for a queens on the upper diagonal
    # on the right side
    i = row - 1
    j = col + 1
    while i >= 0 and j < num:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row=0):
    """This function recursively solves the N queens puzzle"""
    if row == num:
        # prints the solution when there are no more
        # rows to search
        solution = []
        for i in range(num):
            for j in range(num):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
    else:
        for col in range(num):
            if is_queen_safe(board, row, col):
                # place queen if it is safe
                board[row][col] = 1
                # recursively solve for the next row
                solve_nqueens(board, row + 1)
                # backtrack and remove queen
                board[row][col] = 0


if __name__ == '__main__':
    """The main function for the program that accepts an
        integer as a command line argument.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if num < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for item in range(num)] for row in range(num)]
    solve_nqueens(board, 0)
