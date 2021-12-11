__author__ = "Tomasz Rybotycki"

"""
    This script contains solutions to day 1 problems.
"""

def main():
    #p1()
    p2()


def p1():

    count = 0

    with open("in_1.txt", "r") as f:
        prev_line = f.readline()
        line = f.readline()

        while line:
            prev_val = int(prev_line)
            val = int(line)

            if prev_val < val:
                count += 1

            prev_line = line
            line = f.readline()

    print(count)


def p2():

    window_length = 3
    window_vals = []
    window_sum = 0

    counts = 0

    with open("in_1.txt", "r") as f:
        # I assume that number of values is greater than windows length :P
        line = f.readline()
        while len(window_vals) < window_length:
            window_vals.append(int(line))
            line = f.readline()

        prev_val = sum(window_vals)
        window_vals.pop(0)
        line = f.readline()

        while line:
            window_vals.append(int(line))
            val = sum(window_vals)

            if val > prev_val:
                counts += 1

            prev_val = val
            line = f.readline()
            window_vals.pop(0)

    print(counts)



if __name__ == "__main__":
    main()
