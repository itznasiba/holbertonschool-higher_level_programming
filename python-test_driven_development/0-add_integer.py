#!/usr/bin/python3

"""
This module provides a function that adds two integers.
The function handles floats by casting them to integers.
"""

def add_integer(a, b=98):
    # Check if a is a valid number (not NaN or Inf)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")

    # Check if b is a valid number
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
