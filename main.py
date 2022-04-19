import random as rd
from typing import List


class Game:
    def __init__(self) -> None:
        self.board: List[List[int]] = [[0 for _ in range(4)] for _ in range(4)]
        self.random_blocks()
        self.random_blocks(0)

    def random_blocks(self, chance_for_four: float = 0.2) -> None:
        done = True
        for row in self.board:
            if 0 in row:
                done = False
        while not done:
            x, y = rd.randint(0, 3), rd.randint(0, 3)
            if not self.board[y][x] and rd.random() < chance_for_four:
                self.board[y][x] = 4
                done = True
            elif not self.board[y][x]:
                self.board[y][x] = 2
                done = True

    def stack_vertical(self, direction: int, destination: int) -> None:
        for _ in range(3):
            for i in range(4):
                for index, row in enumerate(self.board):
                    if row[i] != 0 and index != destination and self.board[index + direction][i] == 0:
                        self.board[index + direction][i] = self.board[index][i]
                        self.board[index][i] = 0

    def combine_vertical(self, direction: int, destination: int) -> None:
        for i in range(4):
            for index, row in enumerate(self.board):
                if row[i] != 0 and index != destination and self.board[index][i] == self.board[index + direction][i]:
                    self.board[index + direction][i] *= 2
                    self.board[index][i] = 0
                    continue

    def stack_horizontal(self, direction: int, destination: int) -> None:
        for _ in range(3):
            for row in self.board:
                for index, block in enumerate(row):
                    if index != destination and block != 0 and row[index + direction] == 0:
                        row[index + direction] = row[index]
                        row[index] = 0

    def combine_horizontal(self, direction: int, destination: int) -> None:
        for row in self.board:
            for index, block in enumerate(row):
                if row[index] != 0 and index != destination and row[index + direction] == row[index]:
                    row[index] = 0
                    row[index + direction] *= 2
                    continue

    def on_up_key(self) -> None:
        self.stack_vertical(-1, 0)
        self.combine_vertical(-1, 0)
        self.stack_vertical(-1, 0)
        self.random_blocks()

    def on_down_key(self) -> None:
        self.stack_vertical(1, 3)
        self.combine_vertical(1, 3)
        self.stack_vertical(1, 3)
        self.random_blocks()

    def on_right_key(self) -> None:
        self.stack_horizontal(1, 3)
        self.combine_horizontal(1, 3)
        self.stack_horizontal(1, 3)
        self.random_blocks()

    def on_left_key(self) -> None:
        self.stack_horizontal(-1, 0)
        self.combine_horizontal(-1, 0)
        self.stack_horizontal(-1, 0)
        self.random_blocks()

    def lose(self) -> bool:
        for row in self.board:
            if 0 in row:
                return False
        for row in self.board:
            previous = 0
            for tile in row:
                if tile == previous:
                    return False
                previous = tile
        for x in range(4):
            previous = 0
            for y in range(4):
                if self.board[y][x] == previous:
                    return False
                previous = self.board[y][x]
        return True

    def __repr__(self) -> str:
        return str(self.board)

    def __str__(self) -> str:
        display: str = "+-----------------------+"
        for row in self.board:
            display += "\n|"
            for block in row:
                if block == 0:
                    display += "     |"
                else:
                    display += f"{block:^5}|"
            display += "\n+-----------------------+"
        return display


game = Game()

while not game.lose():
    print(game)
    print("Use the WASD keys to play, and hit the space to reset the game.")
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
        game = Game()

print(f"\n\n{game}\n***** GAME OVER! ***** \n")
