#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string == "":
        return 0
    roman_list = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
        }
    total = 0
    for idx in range(len(roman_string) - 1):
        current_value = roman_list[roman_string[idx]]
        next_value = roman_list[roman_string[idx + 1]]
        if current_value < next_value:
            total = total - current_value
        else:
            total = total + current_value
    total = total + roman_list[roman_string[-1]]
    return total
