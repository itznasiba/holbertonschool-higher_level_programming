#!/usr/bin/python3

"""
this module defines an empty square
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    empty class to define square
    """
    def __init__(self, size):
        """
        initialize size
        """
        integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size)**2
