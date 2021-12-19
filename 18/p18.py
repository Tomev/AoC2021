__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 18 problems.
"""


class SnailNumber:
    def __init__(self, left, right, nesting_level = 0):
        self.nesting_level = nesting_level

        if type(left) is list:
            left = SnailNumber(left[0], left[1], nesting_level + 1)

        self.left = left

        if type(right) is list:
            right = SnailNumber(right[0], right[1], nesting_level + 1)

        self.right = right

    def __add__(self, other):
        return SnailNumber(self, other)

    def __str__(self):
        return f"[{str(self.left)}, {str(self.right)}]"

def p1() -> None:
    a = SnailNumber(1, 2)
    b = SnailNumber(3, [4, 5])
    c = a + b
    print(a)
    print(b)
    print(c)
    d = c + c
    print(d)
    print(d.right.right.right.nesting_level)



def main():
    p1()


if __name__ == "__main__":
    main()
