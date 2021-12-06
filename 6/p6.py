__author__ = "Tomasz Rybotycki"

"""
    This script contains 
"""

from typing import List, Dict

class Laternfish():

    def __init__(self, days_to_give_birth: int=8) -> None:
        self.days_to_give_birth = days_to_give_birth

    def give_birth(self):
        self.days_to_give_birth = 6


full_birth_period = 8
birth_period = 6

def get_initial_laternfish() -> List[Laternfish]:

    laternfish = []

    with open("in6.txt", "r") as f:
        line = f.readline()

    for days_to_give_birth in line.split(","):
        laternfish.append(Laternfish(int(days_to_give_birth)))

    return laternfish

def get_initial_laternfish_dict() -> Dict[int, int]:

    laternfish_dict = {}

    for i in range(-1, full_birth_period + 1):
        laternfish_dict[i] = 0

    with open("in6.txt", "r") as f:
        line = f.readline()

    for days_to_give_birth in line.split(","):
        laternfish_dict[int(days_to_give_birth)] += 1


    return laternfish_dict

def p1() -> None:
    laternfish = get_initial_laternfish()
    new_laternfish = []

    observation_days = 256

    for _ in range(observation_days):

        new_laternfish.clear()

        for fish in laternfish:

            fish.days_to_give_birth -= 1

            if fish.days_to_give_birth < 0:
                fish.give_birth()
                new_laternfish.append(Laternfish())

        laternfish.extend(new_laternfish)

    print(len(laternfish))

def p1_fast() -> None:

    laternfish = get_initial_laternfish_dict()

    observation_days = 256

    for _ in range(observation_days):

        for days_to_give_birth in range(full_birth_period + 1):
            laternfish[days_to_give_birth - 1] = laternfish[days_to_give_birth]

        new_fish = laternfish[-1]

        laternfish[full_birth_period] = new_fish
        laternfish[birth_period] += new_fish
        laternfish[-1] = 0

    fish_sum = 0

    for days_to_give_birth in laternfish:
        fish_sum += laternfish[days_to_give_birth]

    print(fish_sum)




def main():
    p1_fast()


if __name__ == "__main__":
    main()
