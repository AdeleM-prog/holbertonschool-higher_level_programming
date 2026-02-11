#!/usr/bin/python3
"""
serialize and deserialize custom Python objects using the pickle module
"""
import pickle


class CustomObject:
    """
    Create a custom Python class named CustomObject
    """
    def __init__(self, name, age, is_student):
        """
        This class should have the following attributes:
        name (a string)
        age (an integer)
        is_student (a boolean)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        method display method to print out the object's attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        This method will take a filename as its parameter.
        Using the pickle module, it will serialize the current
        instance of the object and save it to the provided filename
        """
        try:
            with open(filename, "wb") as f:
                return pickle.dump(self, f)
        except(pickle.UnpicklingError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        This class method will take a filename as its parameter.
        Using the pickle module, it will load and return an instance of
        the CustomObject from the provided filename
        """
        try:
            with open(filename, "rb") as f:
                student_loaded = pickle.load(f)
            return student_loaded
        except(
            OSError, EOFError, pickel.UnpicklingError, FileNotFoundError,
            AttributeError, ImportError, ModuleNotFoundError
        ):
            return None
