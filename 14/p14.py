__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 14 problems.
"""

from typing import Tuple, Dict
from tqdm import tqdm

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


def ps() -> None:
    # This probably can be somehow optimized.
    polymer_template, polymerization_rules = prepare_input()
    steps_number = 40

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



def main():
    ps()


if __name__ == "__main__":
    main()
