__author__ = "Tomasz Rybotycki"

"""
    The aim of this script is to...
"""

from itertools import permutations
from typing import Tuple, Sequence, List, Dict


def prepare_input() -> Tuple[List[List[str]], List[List[str]]]:
    patterns = []
    signals = []

    with open("in8.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "")
            line_parts = line.split(" | ")
            patterns.append(line_parts[0].split(" "))
            signals.append(line_parts[1].split(" "))

    return patterns, signals


def find_number_of_easy_digits_in_sequence(seq: Sequence[List[str]]) -> int:
    number_of_easy_digits = 0
    lengths_of_easy_digits = [2, 3, 4, 7]

    for digits_list in seq:
        for digit in digits_list:
            if lengths_of_easy_digits.__contains__(len(digit)):
                number_of_easy_digits += 1

    return number_of_easy_digits


def p1() -> None:
    patterns, signals = prepare_input()

    number_of_easy_digits = 0
    number_of_easy_digits += find_number_of_easy_digits_in_sequence(signals)

    print(number_of_easy_digits)


def find_easy_numbers_mapping(digits_list: Sequence[str]) -> Dict[str, int]:
    decoding_map = {}

    for digit_str in digits_list:

        result_num = None

        if len(digit_str) == 2:
            result_num = 1
        if len(digit_str) == 3:
            result_num = 7
        if len(digit_str) == 4:
            result_num = 4
        if len(digit_str) == 7:
            result_num = 8

        if not result_num is None:
            decoding_map[digit_str] = result_num

    return decoding_map


def contains(string: str, characters: str) -> bool:
    for character in characters:
        if not string.__contains__(character):
            return False
    return True


def remove_characters(string: str, characters: str) -> str:
    reduced_string = string

    for character in characters:
        reduced_string = reduced_string.replace(character, "")

    return reduced_string


def find_len_6_codes(digits_list: Sequence[str], decoding_map: Dict[str, int]) -> None:
    potential_codes = [code for code in digits_list if len(code) == 6]

    # I will use one and four codes to distinguish between 0, 6 and 9.
    one_code = [code for code in decoding_map if len(code) == 2][0]
    four_code = [code for code in decoding_map if len(code) == 4][0]
    six_code_recognizer = remove_characters(four_code, one_code)

    nine_code = [code for code in potential_codes if contains(code, four_code)][0]
    potential_codes.remove(nine_code)
    six_code = [code for code in potential_codes
                if contains(code, six_code_recognizer)][0]
    potential_codes.remove(six_code)

    # Only 0 is left
    decoding_map[potential_codes[0]] = 0
    decoding_map[six_code] = 6
    decoding_map[nine_code] = 9


def find_len_5_codes(digits_list: Sequence[str], decoding_map: Dict[str, int]) -> None:
    len_5_codes = [code for code in digits_list if len(code) == 5]

    eight_code = [code for code in digits_list if len(code) == 7][0]
    six_code = [code for code in decoding_map if decoding_map[code] == 6][0]
    one_code = [code for code in digits_list if len(code) == 2][0]

    three_code_recognizer = remove_characters(eight_code, one_code)

    three_code = [code for code in len_5_codes
                  if len(remove_characters(code, one_code)) == 3][0]
    len_5_codes.remove(three_code)

    if len(remove_characters(six_code, len_5_codes[0])) == 1:
        five_code = len_5_codes[0]
    else:
        five_code = len_5_codes[1]

    len_5_codes.remove(five_code)
    two_code = len_5_codes[0]

    decoding_map[two_code] = 2
    decoding_map[three_code] = 3
    decoding_map[five_code] = 5


def find_decoding_map(digits_list: Sequence[str]) -> Dict[str, int]:
    decoding_map = find_easy_numbers_mapping(digits_list)

    find_len_6_codes(digits_list, decoding_map)
    find_len_5_codes(digits_list, decoding_map)

    return decoding_map


def decode_digit(digit_code: str, decoding_map: Dict[str, int]) -> int:
    digit_code_permutations = [''.join(p) for p in permutations(digit_code)]

    for code in decoding_map:
        if code in digit_code_permutations:
            return decoding_map[code]

    return -1


def decode(pattern: Sequence[str], signal: Sequence[str]) -> int:
    decoding_map = find_decoding_map(pattern)

    decoded_number = 0

    for i in range(len(signal)):
        decoded_number += pow(10, len(signal) - 1 - i) * \
                          decode_digit(signal[i], decoding_map)

    return decoded_number


def p2() -> None:
    patterns, signals = prepare_input()

    decoded_signals_sum = 0

    for i in range(len(patterns)):
        decoded_signals_sum += decode(patterns[i], signals[i])

    print(decoded_signals_sum)


def main() -> None:
    # p1()
    p2()


if __name__ == "__main__":
    main()
