#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance"""
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
        """Return a string representation of the rectangle object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor for the Rectangle class"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
