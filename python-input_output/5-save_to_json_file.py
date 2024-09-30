#!/usr/bin/python3

"""
contain the code
"""

import json


def save_to_json_file(my_obj, filename):

    """
    contain the save json
    """

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
