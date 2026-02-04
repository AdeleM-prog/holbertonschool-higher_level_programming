#!/usr/bin/python3
""" the module defines inherits_form function"""


def inherits_from(obj, a_class):
    """ a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) the
    specified class ; otherwise False
    """
    if not isinstance(a_class, type):
        return False
    return isinstance(obj, a_class) and type(obj) is not a_class
