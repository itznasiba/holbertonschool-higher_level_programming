#!/usr/bin/python3

"""
3-is_kind_of_class.py
"""


def inherits_from(obj, a_class):
    """
    returns True if obj is instance of a_class  or
    instance of class inherited from
    returns flase otherwise
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
