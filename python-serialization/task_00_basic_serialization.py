#!/usr/bin/python3
"""
json module imported to use json.dump and json.load functions
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    serialize and save data to the specified file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(data, f)


def load_and_deserialize(filename):
    """
    load and deserialize data from the specified file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
