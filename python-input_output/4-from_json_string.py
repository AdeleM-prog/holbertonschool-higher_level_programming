#!/usr/bin/python3
"""
Module json imported to use json.loads function
"""


import json


def from_json_string(my_str):
    """
    a function that returns an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
