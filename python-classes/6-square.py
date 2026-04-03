#!/usr/bin/python3

"""
this module defines an empty square
"""


class Square:
    """
    empty class to define square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__self_position = position

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

    @property
    def position(self):
        """
        position property
        """
        return self.__self_position

    @position.setter
    def position(self, value):
        """
        sets the position value
        """
        if (not isinstance(value, tuple) or len(value != 2)
                or not all (isinstance(num, int) for num in value)
                or not all (num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__self_position = value


    def area(self):
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        print(self.__self_position[1]*"")
        for i in range(self.__size):
            for j in range(self.__size):
                print(self.__self_position[0]*" ",end="")
                print("#", end="")
            print()

