#!/usr/bin/python3

"""
first task serialization
"""

import json


def serialize_and_save_to_file(data, filename):

    """
    serialize a data
    """

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error during data serialization and saving: {e}")


def load_and_deserialize(filename):

    """
    deserialize the data
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error during data loading and deserialization: {e}")
        return None
