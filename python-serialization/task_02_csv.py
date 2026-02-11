#!/usr/bin/python3
"""
reading data from one format (CSV) and converting it
into another format (JSON) using serialization techniques
"""


import csv
import json


def convert_csv_to_json(filename):
    """
    that takes the CSV filename as its parameter and writes
    the JSON data to data.json
    """
    try:
        new_list = []
        with open(filename, "r") as f:
            new_file = csv.DictReader(f)
            """
            Python's csv module to open the CSV file and read the data
            Use the DictReader class to convert each row into a dictionary
            """
            for row in new_file:
                new_list.append(row)
            with open("data.json", "w") as f:
                json.dump(new_list, f)
                return True
                """
                Serialize the list of dictionaries using the json module
                Write the serialized JSON data to data.json
                The function should return True if conversion was successful
                """
    except(FileNotFoundError, OSError):
        """
        Handle exceptions, such as file not found
        Function should return False in this case
        """
        return False
