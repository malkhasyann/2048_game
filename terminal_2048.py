import random
import sys
import copy


class Matrix:
    def __init__(self, data, size=4, score=0):
        self.size = size
        self.data = [[0 for _ in range(size)] for _ in range(size)]
        self.score = 0

    def display(self):
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

