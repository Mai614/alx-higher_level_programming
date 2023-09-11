#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""

def add_new_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attr_name (str): The name of the attribute.
        attr_value (any): The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
