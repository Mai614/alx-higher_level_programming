#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The addition of `a` and `b` as an integer.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Note:
        This function does not import any modules.
    """
    # Check if `a` and `b` are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    # Return the addition of `a` and `b` as an integer
    return a + b
