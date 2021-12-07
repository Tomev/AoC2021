__author__ = "Tomasz Rybotycki"

"""
    The aim of this script is to...
"""

from numpy import array, ndarray, median
from tqdm import tqdm


def get_crabs_positions() -> ndarray:
    with open("in7.txt", "r") as f:
        positions = f.readline().split(",")
        return array(positions, dtype=int)


def p1() -> None:
    crabs_positions = get_crabs_positions()
    used_fuel = 0
    positions_median = median(crabs_positions)

    for position in crabs_positions:
        used_fuel += abs(position - positions_median)

    print(used_fuel)


def p2() -> None:

    crabs_positions = get_crabs_positions()
    used_fuel = 0
    least_used_fuel = None

    for proposed_position in tqdm(range(min(crabs_positions), max(crabs_positions) + 1)):
        used_fuel = 0

        for position in crabs_positions:
            used_fuel += sum([i for i in range(abs(position - proposed_position) + 1)])

        if least_used_fuel is None:
            least_used_fuel = used_fuel

        if least_used_fuel > used_fuel:
            least_used_fuel = used_fuel

    print(least_used_fuel)



def main():
    # p1()  # This actually gave me the right answers, but I'm not sure if it's general.
    p2()


if __name__ == "__main__":
    main()
