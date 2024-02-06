#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes the given string to a text file (UTF-8 encoded)
    and returns the numberof characters written.

    Args:
        filename (str): The name of the file to create or overwite
        text (str): The next to write to the file.

    Returns:
        The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
