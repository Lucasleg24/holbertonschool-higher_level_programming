#!/usr/bin/python3

"""
contain the def for read a file
"""


def read_file(filename=""):

    """
    contain the open function
    """

    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
