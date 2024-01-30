#!/usr/bin/python3
"""This defines a Rectangle."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the are of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle with the character #.
        return the string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for _ in range(self.__height):
           [rect.append("#") for i in range(self.__width)]
           if _ != self.__height -1:
               rect.append("\n")
        return rect
