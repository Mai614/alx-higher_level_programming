#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or a subclass instance of a given class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare the object against.

    Returns:
        bool: True if the object is an instance or a subclass instance of the class,
              False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
