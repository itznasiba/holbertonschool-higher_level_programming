#!/usr/bin/python3

"""
function for appending file
"""


def append_write(filename="", text=""):
    """
    append and write function description
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
