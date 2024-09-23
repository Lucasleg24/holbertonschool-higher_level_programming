#!/usr/bin/python3

"""
contain the function
"""


def inherits_from(obj, a_class):

    """
    contain the code
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
