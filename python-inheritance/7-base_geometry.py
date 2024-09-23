#!/usr/bin/python3

"""
contain the class
"""


class BaseGeometry:

    """
    contain the attribut of the class
    """

    def area(self):

        """
        test exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        test error type and value
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
