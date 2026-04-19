#!/usr/bin/python3
"""
This module contains a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename: The name of the file to read from.

    Returns:
        The Python object represented by the JSON content in the file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
