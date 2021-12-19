__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 18 problems.
"""

from copy import deepcopy
from typing import List
from time import time
from datetime import timedelta

class SnailNumber:
    def __init__(self, left, right, nesting_level = 0, parent = None):
        self.nesting_level = nesting_level
        self.parent = parent

        if type(left) is list:
            left = SnailNumber(left[0], left[1], nesting_level)

        if type(left) is SnailNumber:
            left = deepcopy(left)
            left.parent = self
            left.increase_nesting_level()

        self.left = left

        if type(right) is list:
            right = SnailNumber(right[0], right[1], nesting_level)

        if type(right) is SnailNumber:
            right = deepcopy(right)
            right.parent = self
            right.increase_nesting_level()

        self.right = right

    def __add__(self, other):
        a = deepcopy(self)
        b = deepcopy(other)
        return SnailNumber(a, b)

    def increase_nesting_level(self):
        self.nesting_level += 1

        if type(self.left) == SnailNumber:
            self.left.increase_nesting_level()

        if type(self.right) == SnailNumber:
            self.right.increase_nesting_level()

    def __str__(self):
        return f"[{str(self.left)}, {str(self.right)}]"

    def explode(self) -> bool:

        exploded = False

        if type(self.left) is SnailNumber:

            if self.left.nesting_level == 4:
                exploded = True
                if isinstance(self.right, int):
                    self.right += self.left.right
                else:
                    self.left.increase_first_int_from_right(self.left.right)
                self.left.increase_first_int_from_left(self.left.left)
                self.left = 0
            else:
                exploded = self.left.explode()

        if exploded == True:
            return exploded

        if type(self.right) is SnailNumber:
            if self.right.nesting_level == 4:
                exploded = True
                if isinstance(self.left, int):
                    self.left += self.right.left
                else:
                    self.left.increse_first_int_from_left(self.right.left)
                self.right.increase_first_int_from_right(self.right.right)
                self.right = 0
            else:
                exploded = self.right.explode()

        return exploded

    def get_root(self):
        root = self
        while root.parent is not None:
            root = root.parent
        return root

    def increase_first_int_from_left(self, value: int):

        if self.parent == None:
            return None

        if id(self.parent.left) == id(self):
            return self.parent.increase_first_int_from_left(value)
        else:
            if isinstance(self.parent.left, int):
                self.parent.left += value
            else:
                self.parent.left.increase_rightmost_int(value)

    def increase_rightmost_int(self, value: int):
        if isinstance(self.right, int):
            self.right += value
        else:
            self.right.increase_rightmost_int(value)

    def increase_first_int_from_right(self, value: int):

        if self.parent == None:
            return None

        if id(self.parent.right) == id(self):
            return self.parent.increase_first_int_from_right(value)
        else:
            if isinstance(self.parent.right, int):
                self.parent.right += value
            else:
                self.parent.right.increase_leftmost_int(value)

    def increase_leftmost_int(self, value: int):
        if isinstance(self.left, int):
            self.left += value
        else:
            self.left.increase_leftmost_int(value)

    def split(self):
        split = False

        if isinstance(self.left, SnailNumber):
            split = self.left.split()
        else:
            if self.left > 9:
                split = True
                self.left = SnailNumber(self.left // 2, self.left // 2 + self.left % 2, self.nesting_level + 1, self)

        if split:
            return split

        if isinstance(self.right, SnailNumber):
            split = self.right.split()
        else:
            if self.right > 9:
                split = True
                self.right = SnailNumber(self.right // 2, self.right // 2 + self.right % 2, self.nesting_level + 1, self)

        return split

    def magnitude(self):
        left = right = 0

        if isinstance(self.left, int):
            left += self.left
        else:
            left += self.left.magnitude()

        if isinstance(self.right, int):
            right += self.right
        else:
            right += self.right.magnitude()

        return 3 * left + 2 * right



def prepare_snail_numbers() -> List[SnailNumber]:
    from my_input import nums
    snail_numbers = []

    for num in nums:
        snail_numbers.append(SnailNumber(num[0], num[1]))

    return snail_numbers

def p1() -> None:
    snail_numbers = prepare_snail_numbers()
    current_num = None

    for num in snail_numbers:

        if current_num is None:
            current_num = num
        else:
            current_num += num

        exploded = True
        split = True

        while exploded or split:
            print(current_num)
            exploded = current_num.explode()
            if exploded:
                continue
            split = current_num.split()

    print(current_num)
    print(current_num.magnitude())

def p2() -> None:
    snail_numbers = prepare_snail_numbers()

    max_magnitude = 0

    for i in range(len(snail_numbers)):
        for j in range(i+1, len(snail_numbers)):
            current_num = snail_numbers[i] + snail_numbers[j]

            exploded = True
            split = True

            while exploded or split:
                exploded = current_num.explode()
                if exploded:
                    continue
                split = current_num.split()

            current_magnitude = current_num.magnitude()

            max_magnitude = current_magnitude if current_magnitude > max_magnitude else max_magnitude

            current_num = snail_numbers[j] + snail_numbers[i]

            exploded = True
            split = True

            while exploded or split:
                exploded = current_num.explode()
                if exploded:
                    continue
                split = current_num.split()

            current_magnitude = current_num.magnitude()

            max_magnitude = current_magnitude if current_magnitude > max_magnitude else max_magnitude

    print(max_magnitude)


def main():
    s = time()
    # p1()
    p2()
    print(timedelta(seconds=time() - s))


if __name__ == "__main__":
    main()
