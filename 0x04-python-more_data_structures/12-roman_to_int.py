#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman2 = 0
    for i in range(len(roman_string)):
        if i > 0 and roman1[roman_string[i]] > roman1[roman_string[i - 1]]:
            roman2 += roman1[roman_string[i]] - 2 * \
                        roman1[roman_string[i - 1]]
        else:
            roman2 += roman1[roman_string[i]]
    return roman2
