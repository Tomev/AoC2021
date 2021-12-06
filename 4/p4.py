__author__ = "Tomasz Rybotycki"

"""
    This script contains 
"""

import io
from typing import List, Tuple
from numpy import array, ndarray, where
import numpy

class BingoBoard():

    def __init__(self, data: ndarray) -> None:
        # Data should contain 5 lines, split by spacebars
        self._board = data
        self.has_won = False
        self.win_value = 0

    def cross_number(self, val: int) -> None:
        if self._board.__contains__(val):
            loc = where(self._board == val)
            self._board[loc] = -1

            self._check_for_win(loc)

    def _check_for_win(self, loc) -> None:
        if (self._board[loc[0]] == -1).sum() == len(self._board):
            self.has_won = True
            self.win_value = numpy.sum(self._board) + (self._board == -1).sum()

        self._board = self._board.transpose()

        if (self._board[loc[1]] == -1).sum() == len(self._board):
            self.has_won = True
            self.win_value = numpy.sum(self._board) + (self._board == -1).sum()

    def get_data(self):
        return self._board


def prepare_board(f: io.FileIO) -> BingoBoard:
    board_size = 5
    board = []

    for i in range(board_size):
        line = f.readline()
        if line[0] == " ":
            line = line[1:]
        line = line.replace("  ", " ")
        line = line.replace("\n", "")
        board.append(line.split(" "))

    return BingoBoard(array(board, dtype=int))

def to_int_list(str_list: List[str]) -> List[int]:
    return [int(s) for s in str_list]

def prepare_input() -> Tuple[List[int], List[BingoBoard]]:

    boards = []

    with open("in_4.txt", "r") as f:
        line = f.readline()
        numbers_order = to_int_list(line.split(','))
        line = f.readline()

        while line:
            boards.append(prepare_board(f))
            line = f.readline()

    return numbers_order, boards

def p1():
    numbers_order, boards = prepare_input()

    for number in numbers_order:
        for board in boards:
            board.cross_number(number)
            if board.has_won:
                return number * board.win_value

def p2():
    numbers_order, boards = prepare_input()

    for number in numbers_order:
        for board in boards:
            board.cross_number(number)
            if board.has_won:
                print(number * board.win_value)

        boards = [board for board in boards if board.has_won == False]

def main():
    # print(p1())
    p2()


if __name__ == "__main__":
    main()


