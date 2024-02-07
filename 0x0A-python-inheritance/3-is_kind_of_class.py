#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance
    of the specified class.

    Args:
        obj: Any Python object
        a_class: Class or type to compare against.

    Return:
        bool: True if the object is an instance or inherited instance
        of the specified class
        otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
