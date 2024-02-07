#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""


    def __int__(self, width, height):
        """Initialize a rectangle with given width and height.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the rectangle.
         """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
