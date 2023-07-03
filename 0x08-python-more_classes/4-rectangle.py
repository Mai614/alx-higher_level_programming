#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance with optional width and height"""
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        size = "#" * self.__width
        rect = []
        for index in range(self.__height):
            rect.append(size)
        return "\n".join(rect)

    def __repr__(self):
        """Return a string representation of the rectangle to recreate the instance"""
        return "{}({}, {})".format((type(self).__name__), self.__width, self.__height)

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle, or None if height or width is 0"""
        if self.__height == 0 or self.__width == 0:
            return None
        return (self.__height * 2) + (self.__width * 2)
