#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

sys.argv[1:]
try:
    my_obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_obj = []
for args in sys.argv[1:]:
    my_obj.append(args)
save_to_json_file(my_obj, "add_item.json")
