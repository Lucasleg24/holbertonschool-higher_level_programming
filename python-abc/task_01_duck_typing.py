#!/usr/bin/python3

"""
contain the class
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    """
    contain the abstract class
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    """
    contain circle
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius * self.radius)

    def perimeter(self):
        return abs((2 * self.radius) * pi)


class Rectangle(Shape):

    """
    class rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
