#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple containing the length of a string
    and its first character.
    """
    length = len(sentence)

    # If the sentence is empty, set first character to None
    first_char = sentence[0] if length > 0 else None

    return (length, first_char)
