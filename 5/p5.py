__author__ = "Tomasz Rybotycki"

"""
    This script contains 
"""

from typing import List
from numpy import array
from collections import defaultdict

class Line:
    def __init__(self, start=None, end=None):

        if start is None:
            start = array([0, 0], dtype=int)
        self._start = start

        if end is None:
            end = array([0, 0], dtype=int)
        self._end = end

        self.covered_points = []

    def determine_covered_points(self) -> None:

        if self._start[0] == self._end[0]:
            for i in range(min(self._start[1], self._end[1]),
                           max(self._start[1], self._end[1]) + 1):
                self.covered_points.append((self._start[0], i))
        elif self._start[1] == self._end[1]:
            for i in range(min(self._start[0], self._end[0]),
                           max(self._start[0], self._end[0]) + 1):
                self.covered_points.append((i, self._start[1]))
        else:  # Diagonal
            current_point = list(self._start)
            normalization = abs(self._start[0] - self._end[0])
            step_point = [
                -(self._start[0] - self._end[0]) // normalization,
                -(self._start[1] - self._end[1]) // normalization,
            ]
            self.covered_points.append(tuple(current_point))
            for i in range(normalization):
                current_point[0] += step_point[0]
                current_point[1] += step_point[1]
                self.covered_points.append(tuple(current_point))

def find_1d_lines(file_name: str) -> List[Line]:

    lines = []

    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            points = line.split(" -> ")
            start = array(points[0].split(","), dtype=int)
            end = array(points[1].split(","), dtype=int)

            if start[0] == end[0] or start[1] == end[1]:
                lines.append(Line(start, end))
                lines[-1].determine_covered_points()

            line = f.readline()

    return lines

def find_diagonal_lines(file_name: str) -> List[Line]:
    lines = []

    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            points = line.split(" -> ")
            start = array(points[0].split(","), dtype=int)
            end = array(points[1].split(","), dtype=int)

            dif = start[0] - end[0]

            if start[1] + dif == end[1] or start[1] - dif == end[1]:
                lines.append(Line(start, end))
                lines[-1].determine_covered_points()

            line = f.readline()

    return lines

def p1() -> None:
    input_file = "in_5.txt"
    lines = find_1d_lines(input_file)

    points_coverage = defaultdict(lambda: 0)

    for line in lines:

        for point in line.covered_points:
            points_coverage[point] += 1

    multiply_covered_points_num = 0

    for point in points_coverage:
        if points_coverage[point] > 1:
            multiply_covered_points_num += 1

    print(multiply_covered_points_num)

def p2() -> None:
    input_file = "in_5.txt"
    lines = find_1d_lines(input_file)
    lines.extend(find_diagonal_lines(input_file))

    points_coverage = defaultdict(lambda: 0)

    for line in lines:

        for point in line.covered_points:
            points_coverage[point] += 1

    multiply_covered_points_num = 0

    for point in points_coverage:
        if points_coverage[point] > 1:
            multiply_covered_points_num += 1

    print(multiply_covered_points_num)

def main() -> None:
    # p1()
    p2()



if __name__ == "__main__":
    main()
