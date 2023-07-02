def add_integer(a, b=98):
    """
    Adds two integers and returns the sum.

    :param a: The first integer.
    :param b: The second integer (default value is 98).

    :return: The sum of a and b as an integer.

    :raises TypeError: If a or b is not an integer or float.
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Calculate and return the sum
    return int(a + b)
