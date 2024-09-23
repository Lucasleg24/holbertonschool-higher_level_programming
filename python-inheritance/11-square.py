#!/usr/bin/python3

"""
Contain class inherits from rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    Class representing a square, inherits from Rectangle
    """

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):

        return self.__size ** 2

    def __str__(self):

        return "[Square] {}/{}".format(self.__size, self.__size)
