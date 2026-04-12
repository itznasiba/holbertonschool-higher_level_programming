#!/usr/bin/python3

"""
this module defines an empty square
"""
Rectangle = __import__('9-rectnagle').Rectangle


class Square(Rectangle):
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
