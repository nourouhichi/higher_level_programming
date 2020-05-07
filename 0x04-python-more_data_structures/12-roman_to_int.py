#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    integer = 0
    if len(roman_string) is 1:
        return roman[roman_string]
    for next_c in range(len(roman_string)):
        if (roman[roman_string[next_c]] > roman[roman_string[next_c - 1]])\
                and (next_c > 0):
            integer += roman[roman_string[next_c]]\
                - 2 * roman[roman_string[next_c - 1]]
        else:
            integer += roman[roman_string[next_c]]
    return integer
