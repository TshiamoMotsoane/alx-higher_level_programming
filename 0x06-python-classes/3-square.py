#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
         """Calculates and returns the area of the sqaure."""
         return (self.__size * self.__size)
