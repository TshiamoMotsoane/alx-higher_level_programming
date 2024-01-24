#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """This class defines a sqaure by its size"""


    def __init__(self, size=0):
        """Initializes a new instance of the Square class

        Args:
            size (int): The size of the square
        """
        self.__size = size

        @property
        def size(self):
            """Getter method to get/set the value and the size of the square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        @property
        def position(self, value):
            """Getter method to retrieve the value of the position attribute"""
            return (self.__position)

        @position.setter
        def position(self, value):
            if not (isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
                    raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

        def area(self):
            """Calculate and returns the area of the square."""
            return (self.__size * self.__size)

        def my_print(self):
            """Print the sqaure using the '#' character."""
            if self.__size == 0:
                print("")
                return

            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for l in range(0, self.__size)]
                print("")
