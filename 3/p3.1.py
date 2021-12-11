__author__ = "Tomasz Rybotycki"

"""
    This script contains solution to the first day 3 problem.
"""

def flip(bin):
    flipped = ""

    for c in bin:
        if c == '1':
            flipped += "0"
        else:
            flipped += "1"

    return flipped


def main():

    input_length = 12
    gamma_rate = ""

    for i in range(input_length):
        with open("in_3.1.txt", "r") as f:

            ones = 0
            zeros = 0

            line = f.readline()

            while line:

                if line[i] == '1':
                    ones += 1
                else:
                    zeros += 1

                line = f.readline()

            if ones > zeros:
                gamma_rate += "1"
            else:
                gamma_rate += "0"


    epsilon_rate = int(flip(gamma_rate), 2)
    gamma_rate = int(gamma_rate, 2)

    print(gamma_rate * epsilon_rate)






if __name__ == "__main__":
    main()
