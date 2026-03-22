#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list at a specific position."""
    # Check if the index is negative or out of the upper bounds
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
