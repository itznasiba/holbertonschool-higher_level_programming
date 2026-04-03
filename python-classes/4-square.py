#!/usr/bin/python3

"""
this module defines an empty square
"""


class Square:
    """
    empty class to define square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size)**2
