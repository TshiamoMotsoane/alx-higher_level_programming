#!/usr/bin/python3
"""Defines a square."""


class Square:
    """This class defines a square by its size."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class

        Args:
            size (int): The size of the new aquare.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
