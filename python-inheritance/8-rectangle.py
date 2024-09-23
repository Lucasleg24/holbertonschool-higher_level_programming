#!/usr/bin/python3

"""
contain the code
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    Class that represents a Rectangle, inherits from BaseGeometry
    """

    def __init__(self, width, height):

        """
        init width and height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
