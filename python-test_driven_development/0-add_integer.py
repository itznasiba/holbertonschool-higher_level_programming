#!/usr/bin/python3
"""
This module provides a function that adds two numbers.
The numbers must be integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number.
        b: The second number, defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats, or are NaN/Inf.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
