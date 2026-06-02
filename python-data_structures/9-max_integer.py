#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list without using the built-in max().
    Returns None if the list is empty.
    """
    # Return None instantly if the list is empty
    if not my_list:
        return None

    # Assume the first element is the largest to kick off the comparison
    max_val = my_list[0]

    # Iterate through the rest of the list elements
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val
