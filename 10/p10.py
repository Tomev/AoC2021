__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 10 problems.
"""

from typing import List, Tuple


class NavigationSubsystem():

    def __init__(self) -> None:
        self._open_symbols = ["[", "<", "{", "("]
        self._corresponding_open_symbols = {
            "]": "[", ">": "<", ")": "(", "}": "{"
        }
        self._syntax_scores = {"": 0, ")": 3, "]": 57, "}": 1197, ">": 25137}
        self._autocorrect_scores = {"(": 1, "[": 2, "{": 3, "<": 4}

    def find_syntax_error_score(self, code: List[str]) -> int:

        syntax_error_score = 0

        for line in code:
            illegal_character, _ = self._find_first_illegal_character(line)
            syntax_error_score += self._syntax_scores[illegal_character]

        return syntax_error_score

    def _find_first_illegal_character(self, line: str) -> Tuple[str, List[str]]:
        first_illegal_character = ""
        opened_braces = []

        line = line.replace("\n", "")

        for character in line:

            if character in self._open_symbols:
                opened_braces.append(character)
            else:
                if opened_braces[-1] == self._corresponding_open_symbols[character]:
                    opened_braces.pop(-1)
                else:
                    return character, opened_braces

        return first_illegal_character, opened_braces

    def find_autocorrect_middle_score(self, code: List[str]) -> int:

        autocorrect_errors = []

        for line in code:
            illegal_character, opened_braces = self._find_first_illegal_character(line)

            if illegal_character != "":
                continue

            autocorrect_errors.append(self._get_autocorrect_error(opened_braces))

        autocorrect_errors.sort()

        print(autocorrect_errors)
        return autocorrect_errors[len(autocorrect_errors) // 2]

    def _get_autocorrect_error(self, opened_braces: List[str]) -> int:

        opened_braces.reverse()

        error = 0

        for brace in opened_braces:
            error *= 5
            error += self._autocorrect_scores[brace]

        return error

def prepare_problem_solver() -> Tuple[NavigationSubsystem, List[str]]:
    ns = NavigationSubsystem()
    with open("in10.txt") as f:
        code = f.readlines()

    return ns, code


def p1() -> None:
    ns, code = prepare_problem_solver()
    print(ns.find_syntax_error_score(code))

def p2() -> None:
    ns, code = prepare_problem_solver()
    print(ns.find_autocorrect_middle_score(code))

def main() -> None:
    # p1()
    p2()


if __name__ == "__main__":
    main()
