__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 14 problems.
"""

from typing import Tuple, Dict
from tqdm import tqdm
from collections import defaultdict
from time import time
from datetime import timedelta

def add_polymerization_rule(line: str, rules: Dict[str, str]) -> None:
    line_parts = line.split(" -> ")
    key = line_parts[0]
    # result = key[0] + line_parts[1].strip("\n") + key[1]
    result = key[0] + line_parts[1].strip("\n")
    rules[key] = result


def prepare_input() -> Tuple[str, Dict[str, str]]:

    polymerization_rules = {}

    with open("in14.txt", "r") as f:
        polymer_template = f.readline().strip("\n")

        line = f.readline()
        line = f.readline()

        while line:

            add_polymerization_rule(line, polymerization_rules)
            line = f.readline()

    return polymer_template, polymerization_rules


def p1() -> None:
    # Brute force is 2 slow for 40 steps.
    polymer_template, polymerization_rules = prepare_input()
    steps_number = 10

    for _ in tqdm(range(steps_number)):
        current_polymer = ""

        for i in range(len(polymer_template) - 1):
            current_polymer += polymerization_rules[polymer_template[i:i+2]]

        polymer_template = current_polymer + polymer_template[-1]

    symbols_in_polymer = list(set(polymer_template))
    symbols_occurrences = []

    for symbol in symbols_in_polymer:
        symbols_occurrences.append(polymer_template.count(symbol))

    print(polymer_template)
    print(max(symbols_occurrences) - min(symbols_occurrences))

def p2() -> None:
    s = time()
    polymer_template, polymerization_rules = prepare_input()
    steps_number = 40

    current_pairs = defaultdict(lambda : 0)

    for i in range(len(polymer_template) - 1):
        pair = polymer_template[i] + polymer_template[i + 1]
        current_pairs[pair] += 1

    for _ in tqdm(range(steps_number)):
        new_pairs = defaultdict(lambda : 0)

        for pair in current_pairs:
            new_pairs[polymerization_rules[pair]] += current_pairs[pair]
            new_pairs[polymerization_rules[pair][-1] + pair[-1]] += current_pairs[pair]

        current_pairs = new_pairs

    counts = defaultdict(lambda : 0)

    for pair in current_pairs:
        counts[pair[0]] += current_pairs[pair]
        counts[pair[1]] += current_pairs[pair]

    counts[polymer_template[0]] += 1
    counts[polymer_template[-1]] += 1

    vals = []

    for key in counts:
        vals.append(counts[key])

    print((max(vals) - min(vals)) // 2)
    print(timedelta(seconds=time() - s))


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
