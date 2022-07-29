import random
import sys
import copy

# states
SIZE = 4  # grid size: SIZE x SIZE
MATRIX = [[0 for _ in range(SIZE)] for _ in range(SIZE)]  # the grid
SCORE = 0  # game score

# TODO: in is_gameover func combine_left/right is called which causes a bug of the score

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
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], f' {sep} ', end='')
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

    Parameters:

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


# Moving cells

def move_zeros_right(arr):
    """
    Moves all zeros in the array to the end
    (Utility function for combinations)

    Parameters:
         arr(list): the matrix
    Returns:
        None
    """
    for _ in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] == 0:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def move_zeros_left(arr):
    """
    Moves all zeros in the array to the start
    (Utility function for combinations)

    Parameters:
         arr(list): the matrix
    Returns:
        None
    """
    for _ in range(len(arr) - 1):
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] == 0:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]


def combine_left(arr, score=SCORE):
    """
    Combines the cells of a single row to the left if possible.

    Parameters:
        arr(list): the matrix
    Returns:
        None
    """
    global SCORE

    move_zeros_right(arr)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            arr[i] *= 2
            arr[i + 1] = 0
            SCORE += arr[i]
    move_zeros_right(arr)


def combine_right(arr):
    """
    Combines the cells of a single row to the right if possible.

    Parameters:
        arr(list): the matrix
    Returns:
        None
    """
    global SCORE

    move_zeros_left(arr)
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == arr[i - 1]:
            arr[i] *= 2
            arr[i - 1] = 0
            SCORE += arr[i]
    move_zeros_left(arr)


def move_left(arr):
    """
    Move the grid to the left

    Parameters:
         arr(list): the matrix
    Returns:
        None
    """
    for i in range(len(arr)):
        combine_left(arr[i])


def move_right(arr):
    """
    Move the grid to the right

    Parameters:
         arr(list): the matrix
    Returns:
        None
    """
    for i in range(len(arr)):
        combine_right(arr[i])


def move_up(arr):
    """
    Move the grid to the up

    Parameters:
         arr(list): the matrix
    Returns:
        None
    """
    for j in range(len(arr[0])):
        # get the j-th column
        current_col = []
        for i in range(len(arr)):
            current_col.append(arr[i][j])

        # combine the j-th column
        combine_left(current_col)
        for i in range(len(arr)):
            arr[i][j] = current_col[i]


def move_down(arr):
    """
    Move the grid to the down

    Parameters:
         arr(list): the matrix
    Returns:
        None
    """
    for j in range(len(arr[0])):
        # get the j-th column
        current_col = []
        for i in range(len(arr)):
            current_col.append(arr[i][j])

        # combine the j-th column
        combine_right(current_col)
        for i in range(len(arr)):
            arr[i][j] = current_col[i]


# Game status

def gameover():
    """
    Game Over function for application termination.

    Parameters:

    Returns:
        None
    """
    print('*** GameOver ***')
    print(f'Your Score: {SCORE}')
    sys.exit()


def is_gameover():
    """
    Checks whether the game is over or not.

    Parameters:

    Returns:
        True if game is over, False otherwise
    """
    moved = copy.deepcopy(MATRIX)
    move_left(moved)
    if moved != MATRIX:
        return False
    move_right(moved)
    if moved != MATRIX:
        return False
    move_up(moved)
    if moved != MATRIX:
        return False
    move_down(moved)
    if moved != MATRIX:
        return False
    return True


def is_won(arr):
    """
    Checks whether the game is won.

    Parameters:
         arr(list): the matrix
    Returns:
        True if there is 2048 in the matrix, False otherwise
    """
    for i in range(len(arr)):
        if 2048 in arr[i]:
            return True
    return False


# the game loop

def game_loop():
    add_cell(MATRIX)
    prev_matrix = copy.deepcopy(MATRIX)
    while True:
        print_matrix(MATRIX)

        if is_won(MATRIX):
            print('You reached 2048 and won!')
            print(f'Your Score: {SCORE}')
            answer = input('Would you like to continue? [y/n]')
            if answer.lower() == 'n':
                sys.exit()

        if is_gameover():
            gameover()

        move = input()
        if move == 'a':
            move_left(MATRIX)
        if move == 'w':
            move_up(MATRIX)
        if move == 'd':
            move_right(MATRIX)
        if move == 's':
            move_down(MATRIX)

        if MATRIX != prev_matrix:
            add_cell(MATRIX)
            prev_matrix = copy.deepcopy(MATRIX)


if __name__ == '__main__':
    game_loop()
