#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.
    Modifies the list in-place and returns it.
    """
    # Check if index is within the valid range of the list indices
    if 0 <= idx < len(my_list):
        del my_list[idx]

    return my_list
