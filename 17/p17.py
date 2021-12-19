__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 17 problems.
"""

from time import time
from datetime import timedelta
from typing import Dict, List

class Probe():

    def __init__(self, v_x: int, v_y: int):
        self.x = 0
        self.y = 0

        self.v_x = v_x
        self.v_y = v_y

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

        self.v_y -= 1
        if self.v_x != 0:
            self.v_x = (self.v_x // abs(self.v_x)) * (abs(self.v_x) - 1)


def prepare_input() -> Dict[str, List[int]]:

    trench_data = {}

    with open("in.txt", "r") as f:
        line = f.readline()
        line = line.strip("target area: x=")
        x_y_input = line.split(", y=")
        x_min_max = x_y_input[0].split("..")
        y_min_max = x_y_input[1].split("..")

        trench_data["x"] = [x for x in range(int(x_min_max[0]), int(x_min_max[1]) + 1)]
        trench_data["y"] = [y for y in range(int(y_min_max[0]), int(y_min_max[1]) + 1)]

    return trench_data


def find_min_v_x(trench_data: Dict[str, List[int]]):
    min_x = trench_data["x"][0]

    min_v_x = 1
    max_distance = 1

    while max_distance < min_x:
        min_v_x += 1
        max_distance += min_v_x

    return min_v_x


def ps() -> None:
    trench_data = prepare_input()
    # print(trench_data)

    solutions = []

    min_v_x = find_min_v_x(trench_data)
    max_v_y = 0

    for v_x in range(min_v_x, trench_data["x"][-1] + 1):

        for v_y in range(min(1, trench_data["y"][0]), int(5e2)):  # There's better solution than hard coding it, but fuck it.
            probe = Probe(v_x, v_y)
            while probe.x <= trench_data["x"][-1] and probe.y > trench_data["y"][0]:
                probe.move()
                if trench_data["x"].__contains__(probe.x) and trench_data["y"].__contains__(probe.y):
                    solutions.append((v_x, v_y))
                    max_v_y = v_y if v_y > max_v_y else max_v_y
                    break

    print(f"p1: {sum(list(range(max_v_y + 1)))}")
    print(f"p2: {len(solutions)}")


def main():
    s = time()
    ps()
    print(timedelta(seconds=time() - s))


if __name__ == "__main__":
    main()
