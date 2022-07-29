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

# Generating cells

def find_empty_cells(arr):
    """
    Returns a list of tuples with empty cell indices: (i, j).

    Parameters:
         arr(list): the matrix
    Returns:
        empty_cells(list): list of indices of empty cells
    """
    empty_cells = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def generate_number():
    """
    Randomly returns 2 or 4

    Paramters:
        pass
    Returns:
        value(int): random number
    """
    value = 2 if random.random() <= 0.72 else 4
    return value

def add_cell(arr):
    """
    Generates new cell

    Paramters:
        arr(list): the matrix
    Returns:
         None
    """
    num = generate_number()
    empty_cells = find_empty_cells(arr)
    try:
        cell = random.choice(empty_cells)
        arr[cell[0]][cell[1]] = num
    except IndexError:
        gameover()

# Game status

def gameover():
    print('*** GameOver ***')
    print(f'Your Score: {SCORE}')

def is_gameover():
    pass

def is_won():
    pass
