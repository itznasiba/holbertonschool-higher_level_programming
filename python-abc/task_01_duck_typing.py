#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract Base Class representing an Animal.
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Circle class inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initializes a Circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with a given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    
    Args:
        shape: An object that is expected to have area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
