#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""

class BaseGeometry:
    """
    Base class for geometric shapes.

    Methods:
        area(): Calculate the area of the geometric shape.

    """
    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: This method is not implemented in the base class.

        """
        raise Exception("area() is not implemented")
