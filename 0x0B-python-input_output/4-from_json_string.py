#!/urs/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns the Python object represented by the JSON string."""
    return json.loads(my_str)
