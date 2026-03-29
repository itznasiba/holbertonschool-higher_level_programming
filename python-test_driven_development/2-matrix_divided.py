#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number to divide by (integer or float).

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows in the matrix are not all the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix (list of lists) with the results rounded to 2 decimal places.
    """
    # 1. Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Check if matrix is a valid list of lists of numbers
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg_type)

    # 4. Check if all rows have the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # 5. Perform the division and rounding to create the new matrix
    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)

    return new_matrix
