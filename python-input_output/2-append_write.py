#!/usr/bin/python3

"""
contain code task 2
"""


def append_write(filename="", text=""):
    """
    contain write function with return caracter write
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
