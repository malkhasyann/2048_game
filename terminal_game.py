import random
import sys
import copy

# states
SIZE = 4    # grid size: SIZE x SIZE
MATRIX = [[0 for _ in range(SIZE)] for _ in range(SIZE)]    # the grid
SCORE = 0   # game score


def print_matrix(arr):
    """
    Prints the matrix in rectangular form.

    Parameters:
        arr(list): the matrix

    Returns:
        None
    """
    print(f'Your score: {SCORE}\n')
    sep = '|'
    floor = '-----'
    for i in range(SIZE):
        print(floor, end='')
    print()
    for i in range(len(arr))
        for j in range(len(arr)):
            print(arr[i][j], f' {sep}', end='')
        print()
    for i in range(SIZE):
        print(floor, end='')
    print()