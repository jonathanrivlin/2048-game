import random as rd
from typing import List


class Game:
    def __init__(self):
        self.board = None
        self.reset_game()

    def reset_game(self):
        self.board: List[List[int]] = [[0 for _ in range(4)] for _ in range(4)]
        self.random_blocks()
        self.random_blocks(0)

    def random_blocks(self, chance_for_four: float = 0.2):
        done = False
        while not done:
            x, y = rd.randint(0, 3), rd.randint(0, 3)
            if not self.board[y][x] and rd.random() < chance_for_four:
                self.board[y][x] = 4
                done = True
            elif not self.board[y][x]:
                self.board[y][x] = 2
                done = True

    def show_board(self):
        for row in self.board:
            print("+-----------------------+")
            display: str = "|"
            for block in row:
                if block == 0:
                    display += "     |"
                else:
                    display += f"{block:^5}|"
            print(display)
        print("+-----------------------+")

    def on_up_key(self):
        for _ in range(3):
            for i in range(4):
                for index, row in enumerate(self.board):
                    if row[i] != 0 and index != 0 and self.board[index - 1][i] == 0:
                        self.board[index - 1][i] = self.board[index][i]
                        self.board[index][i] = 0
        for _ in range(3):
            for i in range(4):
                for index, row in enumerate(self.board):
                    if row[i] != 0 and index != 0 and self.board[index][i] == self.board[index - 1][i]:
                        self.board[index - 1][i] *= 2
                        self.board[index][i] = 0
        self.random_blocks()

    def on_down_key(self):
        for _ in range(3):
            for i in range(4):
                for index, row in enumerate(self.board):
                    if row[i] != 0 and index != 3 and self.board[index + 1][i] == 0:
                        self.board[index + 1][i] = self.board[index][i]
                        self.board[index][i] = 0
        for _ in range(3):
            for i in range(4):
                for index, row in enumerate(self.board):
                    if row[i] != 0 and index != 3 and self.board[index + 1][i] == self.board[index][i]:
                        self.board[index + 1][i] *= 2
                        self.board[index][i] = 0
        self.random_blocks()

    def on_right_key(self):
        for _ in range(3):
            for row in self.board:
                for index, block in enumerate(row):
                    if index != 3 and block != 0 and row[index + 1] == 0:
                        row[index + 1] = row[index]
                        row[index] = 0

        for row in self.board:
            for index, block in enumerate(row):
                if row[index] != 0 and index != 3 and row[index + 1] == row[index]:
                    row[index] = 0
                    row[index + 1] *= 2
        self.random_blocks()

    def on_left_key(self):
        for _ in range(3):
            for row in self.board:
                for index, block in enumerate(row):
                    if index != 0 and block != 0 and row[index - 1] == 0:
                        row[index - 1] = block
                        row[index] = 0

        for row in self.board:
            for index, block in enumerate(row):
                if row[index] != 0 and index != 0 and row[index] == row[index - 1]:
                    row[index - 1] *= 2
                    row[index] = 0

        self.random_blocks()


game = Game()

while True:
    game.show_board()
    user_input = input("Enter a direction: ")
    if user_input == 'w':
        game.on_up_key()
    elif user_input == 's':
        game.on_down_key()
    elif user_input == 'a':
        game.on_left_key()
    elif user_input == 'd':
        game.on_right_key()
    elif user_input == ' ':
        game.reset_game()
