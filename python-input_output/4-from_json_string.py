#!/usr/bin/python3
"""
This module contains a function that returns an object
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: The JSON string to be converted into a Python object.

    Returns:
        The Python data structure (list, dict, etc.) represented by my_str.
    """
    return json.loads(my_str)
