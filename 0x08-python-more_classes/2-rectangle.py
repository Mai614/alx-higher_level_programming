#!/usr/bin/python3
"""define a Rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return
        return (self.__height * 2) + (self.__width * 2)
