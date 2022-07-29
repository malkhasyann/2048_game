import random
import sys
import copy


def generate_number():
    """
    Randomly returns 2 or 4

    Parameters:

    Returns:
        value(int): random number
    """
    value = 2 if random.random() <= 0.72 else 4
    return value


def move_zeros_left(row):
    """
    Moves all zeros in the array to the start
    (Utility function for combinations)

    Parameters:
         row(list): the matrix
    Returns:
        None
    """
    for _ in range(len(row) - 1):
        for i in range(len(row) - 1, 0, -1):
            if row[i] == 0:
                row[i], row[i - 1] = row[i - 1], row[i]


def move_zeros_right(row):
    """
    Moves all zeros in the array to the end
    (Utility function for combinations)

    Parameters:
         row(list): the matrix
    Returns:
        None
    """
    for _ in range(len(row) - 1):
        for i in range(len(row) - 1):
            if row[i] == 0:
                row[i], row[i + 1] = row[i + 1], row[i]


class Matrix:
    def __init__(self, size=4):
        """
        Constructor of Matrix

        Parameters:
             self(Matrix)
             size(int): size of the matrix
        Returns:
            None
        """
        self.size = size
        self.data = [[0 for _ in range(size)] for _ in range(size)]
        self.score = 0

    def display(self):
        """
        Displays the matrix

        Parameters:
             self(Matrix)
        Returns:
            None
        """
        print(f'Your score: {self.score}\n')
        sep = '|'
        floor = '-----'
        for i in range(self.size):
            print(floor, end='')
        print()
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                print(self.data[i][j], f' {sep} ', end='')
            print()
        for i in range(self.size):
            print(floor, end='')
        print()

    # Generating cells

    def find_empty_cells(self):
        """
        Returns a list of tuples with empty cell indices: (i, j).

        Parameters:
             self(Matrix)
        Returns:
            empty_cells(list): list of indices of empty cells
        """
        empty_cells = []
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i][j] == 0:
                    empty_cells.append((i, j))
        return empty_cells

    def add_cell(self):
        """
        Generates new cell

        Paramters:
            self(Matrix)
        Returns:
             None
        """
        num = generate_number()
        empty_cells = self.find_empty_cells()
        try:
            cell = random.choice(empty_cells)
            self.data[cell[0]][cell[1]] = num
        except IndexError:
            self.gameover()

    # Moving cells

    def combine_left(self, row):
        """
        Combines the cells of a single row to the left if possible.

        Parameters:
            self(Matrix)
            row(list): a 1D array
        Returns:
            None
        """

        move_zeros_right(row)

        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
                self.score += row[i]

        move_zeros_right(row)

    def combine_right(self, row):
        """
        Combines the cells of a single row to the right if possible.

        Parameters:
            self(Matrix)
            row(list): a 1D array
        Returns:
            None
        """

        move_zeros_left(row)
        for i in range(len(row) - 1, 0, -1):
            if row[i] == row[i - 1]:
                row[i] *= 2
                row[i - 1] = 0
                self.score += row[i]
        move_zeros_left(row)

    def move_left(self):
        """
        Move the grid to the left

        Parameters:
             self(Matrix)
        Returns:
            None
        """
        for i in range(len(self.data)):
            self.combine_left(self.data[i])

    def move_right(self):
        """
        Move the grid to the right

        Parameters:
             self(Matrix)
        Returns:
            None
        """
        for i in range(len(self.data)):
            self.combine_right(self.data[i])

    def move_up(self):
        """
        Move the grid to the up

        Parameters:
             self(Matrix)
        Returns:
            None
        """
        for j in range(len(self.data[0])):
            # get the j-th column
            current_col = []
            for i in range(len(self.data)):
                current_col.append(self.data[i][j])

            # combine the j-th column
            self.combine_left(current_col)
            for i in range(len(self.data)):
                self.data[i][j] = current_col[i]

    def move_down(self):
        """
        Move the grid to the down

        Parameters:
             self(Matrix)
        Returns:
            None
        """
        for j in range(len(self.data[0])):
            # get the j-th column
            current_col = []
            for i in range(len(self.data)):
                current_col.append(self.data[i][j])

            # combine the j-th column
            self.combine_right(current_col)
            for i in range(len(self.data)):
                self.data[i][j] = current_col[i]

    # Game status

    def gameover(self):
        """
        Game Over function for application termination.

        Parameters:

        Returns:
            None
        """
        print('*** GameOver ***')
        print(f'Your Score: {self.score}')
        sys.exit()

    def is_gameover(self):
        """
        Checks whether the game is over or not.

        Parameters:

        Returns:
            True if game is over, False otherwise
        """
        moved = Matrix()
        moved.data = copy.deepcopy(self.data)
        moved.move_left()
        if moved.data != self.data:
            return False
        moved.move_right()
        if moved.data != self.data:
            return False
        moved.move_up()
        if moved.data != self.data:
            return False
        moved.move_down()
        if moved.data != self.data:
            return False
        return True

    def is_won(self):
        """
        Checks whether the game is won.

        Parameters:
            self(Matrix)
        Returns:
            True if there is 2048 in the matrix, False otherwise
        """
        for i in range(len(self.data)):
            if 2048 in self.data[i]:
                return True
        return False


def game_loop():
    size = int(input('Set the size of the grid: '))
    matrix = Matrix(size=size)
    matrix.add_cell()
    prev_matrix = Matrix()
    prev_matrix.data = copy.deepcopy(matrix.data)
    while True:
        matrix.display()

        if matrix.is_won():
            print('You reached 2048 and won!')
            print(f'Your Score: {matrix.score}')
            answer = input('Would you like to continue? [y/n]')
            if answer.lower() == 'n':
                sys.exit()

        if matrix.is_gameover():
            matrix.gameover()

        move = input()
        if move == 'a':
            matrix.move_left()
        if move == 'w':
            matrix.move_up()
        if move == 'd':
            matrix.move_right()
        if move == 's':
            matrix.move_down()

        if matrix.data != prev_matrix.data:
            matrix.add_cell()
            prev_matrix.data = copy.deepcopy(matrix.data)


if __name__ == '__main__':
    game_loop()
