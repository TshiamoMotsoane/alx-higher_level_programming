#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of the specified class.

    Args:
        obj: Any Python object
        a_class: Class or type to compare against.

    Return:
        bool: True if the object is an inherited instance of the specified class
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
