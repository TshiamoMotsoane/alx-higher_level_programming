#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class.

    Args:
        obj: Any Python object
        a_class: Class or type to compare against.

    Return:
        bool: True if the object is exactly an instance of the specified class
        otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
