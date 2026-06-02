#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers using str.format().
    Rows are separated by lines, and numbers within a row are space-separated.
    """
    for row in matrix:
        for i in range(len(row)):
            # Print the integer using format
            print("{:d}".format(row[i]), end="")

            # Print a space only if it's NOT the last element in the row
            if i < len(row) - 1:
                print(" ", end="")

        # Print a newline at the end of each row
        print()
