#!/usr/bin/python3

"""
contain the code
"""
import json


def load_from_json_file(filename):

    """
    contain the json load code
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
