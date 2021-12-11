__author__ = "Tomasz Rybotycki"

"""
    This script contains the solutions to day 11 problems. 
"""

from numpy import ndarray, array, zeros, count_nonzero
from typing import Tuple, List

def prepare_input() -> ndarray:

    lines = []
    input_dimension = 10

    with open("in11.txt", "r") as f:
        line = f.readline()

        while line:
            line = line.strip()
            lines.append([c for c in line])
            line = f.readline()

    input_matrix = array(lines, dtype=int)
    padded_matrix = zeros((input_dimension + 2, input_dimension + 2), dtype=int)

    padded_matrix[1:input_dimension+1, 1:input_dimension+1] = input_matrix

    return padded_matrix


def flash_octopus(position: Tuple[int, int], octopi_energies: ndarray) -> None:
    octopi_energies[position[0] - 1:position[0] +2, position[1] - 1:position[1] + 2] += 1
    octopi_energies[position[0], position[1]] *= -1


def flash_octopi(octopi_energies: ndarray) -> bool:

    has_flashed = False

    for i in range(1, len(octopi_energies) - 1):
        for j in range(1, len(octopi_energies) - 1):
            if octopi_energies[i][j] > 9:
                flash_octopus((i, j), octopi_energies)
                has_flashed = True
                # print("\n\n")
                # print(octopi_energies)

    return has_flashed


def find_flash_octopi_positions(octopi_energies: ndarray) -> List[Tuple[int, int]]:
    flash_octopi_positions = []

    for i in range(1, len(octopi_energies) - 1):
        for j in range(1, len(octopi_energies[i]) - 1):
            if octopi_energies[i][j] <= 0:
                flash_octopi_positions.append((i, j))

    return flash_octopi_positions


def p1() -> None:
    octopi_energies = prepare_input()

    steps_number = 100
    flashes_count = 0

    for step in range(steps_number):
        # Update energies
        octopi_energies[1:len(octopi_energies) - 1, 1:len(octopi_energies) - 1] += 1

        # Proceed with the flashes.
        has_flashed = True

        while has_flashed:
            has_flashed = flash_octopi(octopi_energies)

        # Count octopi that flashed and set their counter to 0.
        flash_octopi_positions = find_flash_octopi_positions(octopi_energies)
        flashes_count += len(flash_octopi_positions)

        for position in flash_octopi_positions:
            octopi_energies[position[0]][position[1]] = 0

    print(flashes_count)


def p2() -> None:
    octopi_energies = prepare_input()

    step_number = 0

    while True:
        step_number += 1
        # Update energies
        octopi_energies[1:len(octopi_energies) - 1, 1:len(octopi_energies) - 1] += 1

        # Proceed with the flashes.
        has_flashed = True

        while has_flashed:
            has_flashed = flash_octopi(octopi_energies)

        # Count octopi that flashed and set their counter to 0.
        flash_octopi_positions = find_flash_octopi_positions(octopi_energies)

        if len(flash_octopi_positions) == 100:
            break

        for position in flash_octopi_positions:
            octopi_energies[position[0]][position[1]] = 0



    print(step_number)

def main():
    # p1()
    p2()


if __name__ == "__main__":
    main()
