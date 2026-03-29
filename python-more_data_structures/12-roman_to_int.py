#!/usr/bin/python3
"""
Module for Roman to Integer conversion
"""
def roman_to_int(roman_string):
    # Validation check
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionary of Roman numeral values
    rom_val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(roman_string)

    for i in range(n):
        # Get the value of the current character
        current_val = rom_val.get(roman_string[i], 0)

        # Check if there is a 'next' character and compare values
        if i + 1 < n:
            next_val = rom_val.get(roman_string[i + 1], 0)
            if current_val < next_val:
                # Subtraction rule applies (e.g., IV, IX, XL)
                total -= current_val
            else:
                total += current_val
        else:
            # Last character is always added
            total += current_val

    return total
