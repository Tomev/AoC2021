__author__ = "Tomasz Rybotycki"

"""
    This script contains the solutions to day 12 problems. 
"""

from typing import DefaultDict, List
from collections import defaultdict


def prepare_input() -> DefaultDict[str, List[str]]:

    connections_map = defaultdict(lambda: list())

    with open("in12.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace("\n", "")
        parts = line.split("-")

        connections_map[parts[0]].append(parts[1])
        connections_map[parts[1]].append(parts[0])

    return connections_map


def find_possible_paths(connections_map: DefaultDict[str, List[str]],
                        current_path: List[str] = None) -> List[List[str]]:

    possible_paths = []

    if len(current_path) == 0:
        current_path.append("start")

    if current_path[-1] == "end":
        return [current_path]

    for possible_room in connections_map[current_path[-1]]:

        if not current_path.__contains__(possible_room) or possible_room.lower() != possible_room:
            path = current_path.copy()
            path.append(possible_room)
            possible_paths.extend(find_possible_paths(connections_map, path))

    return possible_paths


def p1() -> None:
    connections_map = prepare_input()

    paths = find_possible_paths(connections_map, [])

    print(len(paths))


def find_possible_paths_2(connections_map: DefaultDict[str, List[str]],
                        current_path: List[str] = None) -> List[List[str]]:

    possible_paths = []

    if len(current_path) == 0:
        current_path.append("start")

    if current_path[-1] == "end":
        return [current_path]

    for possible_room in connections_map[current_path[-1]]:

        if possible_room == "start":
            continue

        path = current_path.copy()

        if possible_room.lower() == possible_room and current_path.count(possible_room) > 0 and possible_room != "end":

            if path[0] == '0':
                continue
            else:
                path.insert(0, '0')

        path.append(possible_room)
        possible_paths.extend(find_possible_paths_2(connections_map, path))

    return possible_paths


def p2() -> None:
    connections_map = prepare_input()

    paths = find_possible_paths_2(connections_map, [])

    print(len(paths))


def main() -> None:
    # p1()
    p2()


if __name__ == "__main__":
    main()
