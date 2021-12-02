__author__ = "Tomasz Rybotycki"

"""
    This script contains 
"""

def up(val, position):
    position["depth"] -= val

def down(val, position):
    position["depth"] += val

def forward(val, position):
    position["horizontal"] += val

def p1():

    movement = {
        "forward": forward,
        "down": down,
        "up": up
    }

    position = {"horizontal": 0, "depth": 0}

    with open("in_2.1.txt", "r") as f:
        line = f.readline()

        while line:

            direction, value = line.split(" ")[0], int(line.split(" ")[1])
            movement[direction](value, position)

            line = f.readline()


    print(position["depth"] * position["horizontal"])





if __name__ == "__main__":
    p1()
