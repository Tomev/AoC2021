__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 13 problems.
"""

from numpy import ndarray, zeros, flip
from typing import List, Dict, Tuple


def get_folding_instructions(input_file: str) -> List[str]:

    folding_lines = []

    with open(input_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.__contains__("fold"):
            folding_lines.append(line.split(" ")[-1])

    return folding_lines


def get_input_shape(file_name: str) -> List[int]:
    x = y = 0

    with open(file_name, "r") as f:

        while x == 0 or y == 0:
            line = f.readline()

            if line.__contains__('y'):
                y = int(line.split("y=")[1])

            if line.__contains__('x'):
                x = int(line.split("x=")[1])

    return [2 * y + 1, 2 * x + 1]


def prepare_input_array(shape: List[int], input_file: str) -> ndarray:

    input_array = zeros(shape, dtype=int)

    with open(input_file, "r") as f:
        lines = f.readlines()

    for line in lines:

        if line == "\n":
            break

        line = line.strip()

        y, x = line.split(",")

        input_array[int(x)][int(y)] = 1

    return input_array


def prepare_input() -> Tuple[ndarray, List[str]]:

    input_file = "in13.txt"

    shape = get_input_shape(input_file)

    input_array = prepare_input_array(shape, input_file)

    folding_instructions = get_folding_instructions(input_file)

    return input_array, folding_instructions


def fold_horizontal(transparent_paper: ndarray, instruction: str) -> ndarray:
    split_index = int(instruction.split("=")[-1])
    upper = transparent_paper[0:split_index]
    bottom = transparent_paper[split_index+1: len(transparent_paper)]

    bottom = flip(bottom, axis=0)

    for i in range(len(upper)):
        for j in range(len(upper[i])):
            if bottom[i][j] == 1:
               upper[i][j] = 1

    return upper


def fold_vertical(transparent_paper: ndarray, instruction: str) -> ndarray:

    split_index = int(instruction.split("=")[-1])
    left = transparent_paper[:, 0:split_index]
    right = transparent_paper[:, split_index + 1: len(transparent_paper[0])]

    right = flip(right, axis=1)

    for i in range(len(left)):
        for j in range(len(left[i])):
            if right[i][j] == 1:
                left[i][j] = 1

    return left


def fold(transparent_paper: ndarray, instruction: str) -> ndarray:
    if instruction.__contains__("x"):
        return fold_vertical(transparent_paper, instruction)
    else:
        return fold_horizontal(transparent_paper, instruction)


def p1() -> None:
    transparent_paper, folding_instructions = prepare_input()

    folded = fold(transparent_paper, folding_instructions[0])

    print(sum(sum(folded)))


def p2() -> None:
    transparent_paper, folding_instructions = prepare_input()

    folded = transparent_paper

    for instruction in folding_instructions:
        folded = fold(folded, instruction)

    print(folded)


def main() -> None:
    # p1()
    p2()

if __name__ == "__main__":
    main()
