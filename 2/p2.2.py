__author__ = "Tomasz Rybotycki"

"""
    This script contains solution to the second day 2 problem.
"""

def up(val, position):
    position["aim"] -= val

def down(val, position):
    position["aim"] += val

def forward(val, position):
    position["horizontal"] += val
    position["depth"] += position["aim"] * val

def p2():

    movement = {
        "forward": forward,
        "down": down,
        "up": up
    }

    position = {"horizontal": 0, "depth": 0, "aim": 0}

    with open("in_2.1.txt", "r") as f:
        line = f.readline()

        while line:

            direction, value = line.split(" ")[0], int(line.split(" ")[1])
            movement[direction](value, position)

            line = f.readline()


    print(position["depth"] * position["horizontal"])

if __name__ == "__main__":
    p2()
