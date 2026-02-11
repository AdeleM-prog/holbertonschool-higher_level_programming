#!/usr/bin/python3
"""
a simple implementation of a serialization and deserialization mechanism
"""


class Student:
    """
    a class Student that defines a student by:
    Public instance attributes: first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public instance that retrieves a dictionary representation
        of a Student instance
        """
        if isinstance(attrs, list) and all(type(x) is str for x in attrs):
            student_dict = dict()
            for key in attrs:
                if key in self.__dict__:
                    student_dict[key] = self.__dict__[key]
                    """
                    If attrs is a list of strings, only attribute names
                    contained in this list must be retrieved
                    """
            return student_dict

        return self.__dict__

    def reload_from_json(self, json):
        """
        function that replaces all attributes of the Student instance
        A dictionary key will be the public attribute name
    A dictionary value will be the value of the public attribute
        """
        for key, value in json.items():
            if key in self.__dict__:
                setattr(self, key, value)
