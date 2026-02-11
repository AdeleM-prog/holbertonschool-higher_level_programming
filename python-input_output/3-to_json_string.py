#!/usr/bin/python3
"""
Module json imported to deal with json.dumps function
"""


import json


def to_json_string(my_obj):
    """
    a function that returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
