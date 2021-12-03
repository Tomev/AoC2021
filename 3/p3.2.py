__author__ = "Tomasz Rybotycki"

"""
    This script contains 
"""

input_length = 12

def flip_c(c):
    if c == "1":
        return "0"
    else:
        return "1"

def find_submarine_rating(co2 = False):

    input_numbers = get_initial_input()
    rating = ""

    for position in range(input_length):
        most_common_bit = find_most_common_bit(input_numbers, position)

        if co2:
            most_common_bit = flip_c(most_common_bit)

        input_numbers = [num for num in input_numbers if num[position] == most_common_bit]

        if len(input_numbers) == 1:
            rating = input_numbers[0]
            break

    return int(rating, 2)

def get_initial_input():
    with open("in_3.1.txt", "r") as f:
        return f.readlines()

def find_most_common_bit(input_numbers, position):
    ones = 0
    zeros = 0

    for input_number in input_numbers:

        if input_number[position] == "1":
            ones += 1
        else:
            zeros += 1

    if ones >= zeros:
        return "1"

    return "0"

def main():
    oxygen_rating = find_submarine_rating()
    co2_scrubber_rating = find_submarine_rating(co2=True)
    print(oxygen_rating * co2_scrubber_rating)



if __name__ == "__main__":
    main()
