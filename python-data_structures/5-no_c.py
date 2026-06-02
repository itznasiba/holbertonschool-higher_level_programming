#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from a string.
    """
    # Create a new list containing only characters that are not 'c' or 'C'
    filtered_chars = [char for char in my_string if char != 'c' and char != 'C']
    
    # Join the characters back into a single string
    return "".join(filtered_chars)
