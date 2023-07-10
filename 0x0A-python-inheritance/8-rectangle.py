#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""

class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape.

    This class inherits from the BaseGeometry class and provides specific
    functionality for a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
