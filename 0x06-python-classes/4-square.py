#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """This class defines a sqaure  y its size."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Getter mothod to get/set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size muust be an integer")
        elif value < 0:
            raise ValueError("size must >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return (self.__size * self.__size)
