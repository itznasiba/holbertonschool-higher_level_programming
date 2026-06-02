#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.
    Returns a new list containing True or False corresponding to each element.
    """
    if not my_list:
        return []

    # Use a list comprehension to evaluate numbers using the modulo operator
    return [num % 2 == 0 for num in my_list]
