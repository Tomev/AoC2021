__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 15 problems.
    
    I'm using implementation of Dijkstra's algorithm from:
    
    https://www.geeksforgeeks.org/shortest-path-weighted-graph-weight-edge-1-2/
    
    Later I changed it so some other implementation, sorry I don't remember from where!
"""

from collections import defaultdict
from typing import List
from time import time
from datetime import timedelta


class Graph():
    def __init__(self):
        """
         self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight, w2):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = w2


def add_edges(graph: Graph, lines: List[str]) -> None:
    connections = []
    for line in lines:
        connections.append(line.strip("\n"))

    lines = connections

    # print(lines)

    for i in range(len(lines) - 1):
        for j in range(len(lines[i]) - 1):
            graph.add_edge(i * len(lines[i]) + j, i * len(lines[i]) + (j + 1), int(lines[i][j + 1]), int(lines[i][j]))
            graph.add_edge(i * len(lines[i]) + j, (i + 1) * len(lines[i]) + j, int(lines[i + 1][j]), int(lines[i][j]))

    for i in range(len(lines) - 1):
        graph.add_edge(i * len(lines[0]) + len(lines[0]) - 1,  (i + 2) * len(lines[0]) - 1, int(lines[i+1][-1]), int(lines[i][-1]))

    for j in range(len(lines[-1]) -1):
        graph.add_edge((len(lines) - 1) * len(lines[0]) + j, (len(lines) - 1) * len(lines[0]) + j + 1, int(lines[-1][j + 1]), int(lines[len(lines) - 1][j]))


def prepare_input() -> Graph:
    with open("in.txt", "r") as f:
        lines = f.readlines()

    graph = Graph()

    add_edges(graph, lines)

    return graph


def extend_line(line: str) -> str:
    extended_line = ""

    for i in range(5):
        for val in line:
            val = int(val) + i
            val = val % 10 + 1 if val > 9 else val
            extended_line += str(val)

    return extended_line


def extend_downward(lines: List[str]) -> List[str]:
    downward_extended_lines = []

    for i in range(5):

        for line in lines:

            incremented_line = ""

            for val in line:
                val = int(val) + i
                val = val % 10 + 1 if val > 9 else val
                incremented_line += str(val)

            downward_extended_lines.append(incremented_line)


    return downward_extended_lines


def prepare_input_2() -> Graph:
    with open("in.txt", "r") as f:
        lines = f.readlines()

    extended_lines = []

    for line in lines:
        extended_lines.append(extend_line(line.strip("\n")))

    extended_lines = extend_downward(extended_lines)

    graph = Graph()

    add_edges(graph, extended_lines)

    return graph


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if
                             node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


def p1():
    graph = prepare_input()
    path = dijsktra(graph, 0, max([vertex for vertex in graph.edges]))
    path_len = 0

    for i in range(len(path) - 1):
        path_len += graph.weights[(path[i], path[i + 1])]

    print(path_len)


def p2():
    s = time()
    graph = prepare_input_2()
    path = dijsktra(graph, 0, max([vertex for vertex in graph.edges]))
    path_len = 0

    for i in range(len(path) - 1):
        path_len += graph.weights[(path[i], path[i + 1])]

    print(path_len)
    print(timedelta(seconds=time() - s))



def main():
    # p1()
    p2()


if __name__ == "__main__":
    main()
