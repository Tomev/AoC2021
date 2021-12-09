__author__ = "Tomasz Rybotycki"

"""
    This script contains 
"""

from numpy import ndarray, array
from typing import List

def prepare_input() -> ndarray:

    heightmap = []

    with open("in9.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        heightmap.append([c for c in line])

    heightmap = array(heightmap, dtype=int)

    return heightmap


def find_inner_risk_levels(risk_levels: List[int], heightmap: ndarray) -> None:
    for i in range(1, len(heightmap) - 1):
        for j in range(1, len(heightmap[i]) - 1):

            current_height = heightmap[i][j]
            neighbour_heights = array([
                heightmap[i][j + 1], heightmap[i][j - 1],
                heightmap[i + 1][j], heightmap[i - 1][j]
            ], dtype=int)

            if all(current_height < neighbour_heights):
                risk_levels.append(current_height + 1)


def find_corner_risk_levels(risk_levels: List[int], heightmap: ndarray) -> None:
    i_max = len(heightmap) - 1
    j_max = len(heightmap[0]) - 1

    if all(heightmap[0][0] < array([heightmap[0][1], heightmap[1][0]])):
        risk_levels.append(1 + heightmap[0][0])

    if all(heightmap[i_max][j_max] < array([heightmap[i_max][j_max - 1],
                                            heightmap[i_max - 1][j_max]])):
        risk_levels.append(1 + heightmap[i_max][j_max])

    if all(heightmap[i_max][0] < array([heightmap[i_max][1], heightmap[i_max - 1][0]])):
        risk_levels.append(1 + heightmap[i_max][0])

    if all(heightmap[0][j_max] < array([heightmap[0][j_max - 1], heightmap[1][j_max]])):
        risk_levels.append(1 + heightmap[0][j_max])


def find_vertical_non_corner_edge_risk_levels(risk_levels: List[int],
                                              heightmap: ndarray)  -> None:
    i_max = len(heightmap) - 1
    j_max = len(heightmap[0]) - 1

    for i in range(1, i_max):
        height = heightmap[i][0]
        neighbour_heights = array([heightmap[i][1], heightmap[i - 1][0],
                                   heightmap[i + 1][0]])

        if all(height < neighbour_heights):
            risk_levels.append(1 + height)

        height = heightmap[i][j_max]
        neighbour_heights = array([heightmap[i - 1][j_max], heightmap[i][j_max - 1],
                                   heightmap[i + 1][j_max]])

        if all(height < neighbour_heights):
            risk_levels.append(1 + height)

def find_horizontal_non_corner_edge_risk_levels(risk_levels: List[int],
                                                heightmap: ndarray)  -> None:
    i_max = len(heightmap) - 1
    j_max = len(heightmap[0]) - 1

    for j in range(1, j_max):
        height = heightmap[0][j]
        neighbour_heights = array([heightmap[0][j - 1], heightmap[1][j],
                                   heightmap[0][j + 1]])

        if all(height < neighbour_heights):
            risk_levels.append(1 + height)

        height = heightmap[i_max][j]
        neighbour_heights = array([heightmap[i_max][j + 1], heightmap[i_max - 1][j],
                                   heightmap[i_max][j - 1]])

        if all(height < neighbour_heights):
            risk_levels.append(1 + height)

def find_non_corner_edge_risk_levels(risk_levels: List[int], heightmap: ndarray) \
    -> None:

    find_vertical_non_corner_edge_risk_levels(risk_levels, heightmap)
    find_horizontal_non_corner_edge_risk_levels(risk_levels, heightmap)


def find_outer_risk_levels(risk_levels: List[int], heightmap: ndarray) -> None:
    find_corner_risk_levels(risk_levels, heightmap)
    find_non_corner_edge_risk_levels(risk_levels, heightmap)


def find_risk_levels(heightmap: ndarray) -> List[int]:
    risk_levels = []

    find_outer_risk_levels(risk_levels, heightmap)
    find_inner_risk_levels(risk_levels, heightmap)

    return risk_levels


def p1() -> None:
    heightmap = prepare_input()

    risk_levels = find_risk_levels(heightmap)

    print(sum(risk_levels))


def find_basin_size(starting_point: List[int], heightmap: ndarray) -> int:
    special_heights = [-1, 9]

    if special_heights.__contains__(heightmap[starting_point[0]][starting_point[1]]):
        return 0

    # Count and mark current point.
    basin_size = 1
    heightmap[starting_point[0]][starting_point[1]] = -1

    if starting_point[0] < len(heightmap) - 1:
        starting_point[0] += 1
        basin_size += find_basin_size(starting_point, heightmap)
        starting_point[0] -= 1

    if starting_point[0] > 0:
        starting_point[0] -= 1
        basin_size += find_basin_size(starting_point, heightmap)
        starting_point[0] += 1

    if starting_point[1] < len(heightmap[0]) - 1:
        starting_point[1] += 1
        basin_size += find_basin_size(starting_point, heightmap)
        starting_point[1] -= 1

    if starting_point[1] > 0:
        starting_point[1] -= 1
        basin_size += find_basin_size(starting_point, heightmap)
        starting_point[1] += 1

    return basin_size


def find_basin_sizes(heightmap: ndarray) -> List[int]:
    basin_sizes = []
    special_heights = [-1, 9]

    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if not special_heights.__contains__(heightmap[i][j]):
                basin_sizes.append(find_basin_size([i, j], heightmap))

    return basin_sizes

def p2() -> None:
    heightmap = prepare_input()

    basin_sizes = sorted(find_basin_sizes(heightmap))


    if len(basin_sizes) > 2:
        print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
    else:
        print("Error in the input or method.")



def main():
    # p1()
    p2()


if __name__ == "__main__":
    main()
