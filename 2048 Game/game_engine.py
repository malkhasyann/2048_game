import random
import copy


def generate_number():
    value = 2 if random.random() <= 0.72 else 4
    return value


def move_zeros_left(row):
    for _ in range(len(row) - 1):
        for i in range(len(row) - 1, 0, -1):
            if row[i] == 0:
                row[i], row[i - 1] = row[i - 1], row[i]


def move_zeros_right(row):
    for _ in range(len(row) - 1):
        for i in range(len(row) - 1):
            if row[i] == 0:
                row[i], row[i + 1] = row[i + 1], row[i]


class Matrix:
    def __init__(self, size=4):
        self.size = size
        self.data = [[0 for _ in range(size)] for _ in range(size)]
        self.score = 0
        self.prev_data = copy.deepcopy(self.data)

    # Generating cells

    def find_empty_cells(self):
        empty_cells = []
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i][j] == 0:
                    empty_cells.append((i, j))
        return empty_cells

    def add_cell(self):
        num = generate_number()
        empty_cells = self.find_empty_cells()
        try:
            cell = random.choice(empty_cells)
            self.data[cell[0]][cell[1]] = num
        except IndexError:
            pass

    # Moving cells

    def combine_left(self, row):
        move_zeros_right(row)

        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
                self.score += row[i]

        move_zeros_right(row)

    def combine_right(self, row):
        move_zeros_left(row)
        for i in range(len(row) - 1, 0, -1):
            if row[i] == row[i - 1]:
                row[i] *= 2
                row[i - 1] = 0
                self.score += row[i]
        move_zeros_left(row)

    def move_left(self):
        self.prev_data = copy.deepcopy(self.data)
        for i in range(len(self.data)):
            self.combine_left(self.data[i])

    def move_right(self):
        self.prev_data = copy.deepcopy(self.data)
        for i in range(len(self.data)):
            self.combine_right(self.data[i])

    def move_up(self):
        self.prev_data = copy.deepcopy(self.data)
        for j in range(len(self.data[0])):
            current_col = []
            for i in range(len(self.data)):
                current_col.append(self.data[i][j])

            self.combine_left(current_col)
            for i in range(len(self.data)):
                self.data[i][j] = current_col[i]

    def move_down(self):
        self.prev_data = copy.deepcopy(self.data)
        for j in range(len(self.data[0])):
            current_col = []
            for i in range(len(self.data)):
                current_col.append(self.data[i][j])

            self.combine_right(current_col)
            for i in range(len(self.data)):
                self.data[i][j] = current_col[i]

    # Game status

    def is_gameover(self):
        if not self.find_empty_cells():
            for i in range(len(self.data)):
                for j in range(len(self.data) - 1):
                    if self.data[i][j] == self.data[i][j + 1]:
                        return False

            for j in range(len(self.data)):
                for i in range(len(self.data) - 1):
                    if self.data[i][j] == self.data[i + 1][j]:
                        return False
            return True

    def is_won(self):
        for i in range(len(self.data)):
            if 2048 in self.data[i]:
                return True
        return False
