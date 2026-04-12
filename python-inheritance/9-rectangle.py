#!/usr/bin/python3

"""
this module defines an empty square
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle class
    """

    def __init__(self, width, height):
        """
        initialize rectangle
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

        def area(self):
            """
            calculates area
            """
            return self.__width*self.__height

        def __str__(self):
            """
            str underscore functions
            """
            return "[Rectangle] {}/{}".format(self.__width, self.__height)
