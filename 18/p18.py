__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 18 problems.
"""

from copy import deepcopy

class SnailNumber:
    def __init__(self, left, right, nesting_level = 0, parent = None):
        self.nesting_level = nesting_level
        self.parent = parent

        if type(left) is list:
            left = SnailNumber(left[0], left[1], nesting_level, self)

        if type(left) is SnailNumber:
            left = deepcopy(left)
            left.increase_nesting_level()

        self.left = left

        if type(right) is list:
            right = SnailNumber(right[0], right[1], nesting_level, self)

        if type(right) is SnailNumber:
            right = deepcopy(right)
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
                self.right += self.left.right
                self.left = 0
            else:
                exploded = self.left.explode()

        if type(self.right) is SnailNumber:
            if self.right.nesting_level == 4:
                exploded = True
                self.left += self.right.left
                self.right = 0
            else:
                exploded = self.right.explode() or exploded

        return exploded

    def get_root(self):
        root = self
        while root.parent is not None:
            root = root.parent
        return root

def p1() -> None:
    a = SnailNumber([6,[5,[4,[3,2]]]],1)
    a_root = a.get_root()
    print(a_root)
    print(a.left.get_root())
    a_r_r_root = a.left.right.right.right.get_root()
    print(a_r_r_root)




def main():
    p1()


if __name__ == "__main__":
    main()
