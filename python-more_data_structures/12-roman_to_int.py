#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    rom_dir = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(roman_string)):
        current = rom_dir[roman_string[i]]
        if i + 1 < len(roman_string):
            next_val = rom_dir[roman_string[i + 1]]
        if i + 1 < len(roman_string) and current < next_val:
            total -= current
        else:
            total += current
    return total
