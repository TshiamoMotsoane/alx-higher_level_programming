#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a file (UTF8)

    Args:
        filename (str): The name of the file to create or overwrite.
        text (str): The string to write to the file.

    Returns:
        The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

