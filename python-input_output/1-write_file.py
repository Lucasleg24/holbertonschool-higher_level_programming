#!/usr/bin/python3

"""
contain def for write function
"""


def write_file(filename="", text=""):

    """
    contain write function with return caracter write
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
