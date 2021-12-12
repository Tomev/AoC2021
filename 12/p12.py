__author__ = "Tomasz Rybotycki"

"""
    This script contains the solutions to day 11 problems. 
"""

from typing import DefaultDict, List
from collections import defaultdict


def prepare_input() -> DefaultDict[str, List[str]]:

    connections_map = defaultdict(lambda: list())

    with open("test.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace("\n", "")
        parts = line.split("-")

        connections_map[parts[0]].append(parts[1])
        connections_map[parts[1]].append(parts[0])

    return connections_map


def find_possible_paths(connections_map: DefaultDict[str, List[str]],
                        current_path: List[List[str]] = None) -> List[List[str]]:

    possible_paths = []

    if current_path is None:
        current_path = ["start"]

    if current_path[-1] == "end":
        return [current_path]

    for possible_room in connections_map[current_path[-1]]:
        if current_path.__contains__(possible_room):
            possible_paths.append(current_path)

    return possible_paths


def p1() -> None:
    connections_map = prepare_input()

    paths = find_possible_paths(None, connections_map)

    print(len(paths))


def main() -> None:
    p1()


if __name__ == "__main__":
    main()