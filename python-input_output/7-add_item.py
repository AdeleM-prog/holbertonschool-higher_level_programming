#!/usr/bin/python3

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Module sys imported to use the sys.argv function
import'5-save_to_json_file' file to use the save_to_json_file function
import '6-load_from_json_file' file to use load_from_json_file function
"""

sys.argv[1:]
try:
    my_obj = load_from_json_file("add_item.json")
    """
    must use your function load_from_json_file from 6-load_from_json_file.py
    The list must be saved as a JSON representation in file named add_item.json
    """
except FileNotFoundError:
    my_obj = []
    """If the file doesn't exist, it should be created"""
for args in sys.argv[1:]:
    my_obj.append(args)
save_to_json_file(my_obj, "add_item.json")
"""You must use your function save_to_json_file from 5-save_to_json_file.py"""
