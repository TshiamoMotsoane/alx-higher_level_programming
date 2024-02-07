#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Public instance method that raises an Exception with the message
        'area() is not implemented'.
        """

    def integer_validator(self, name, value):
        """Public instance method that validates the given value.

        Args:
            name (str): The name of the value being validated
            value: The value to be validated

        Raises:
            TypeError if the value iss not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
        if value <= 0:
                raise  ValueError("{} must be greater than 0".format(name))
