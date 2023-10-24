#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0  # Class attribute to keep track of the number of instances
    print_symbol = "#"  # Symbol used to represent the rectangle when printing

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the number of instances

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        size = str(self.print_symbol) * self.__width
        rect = []
        for index in range(self.__height):
            rect.append(size)
        return "\n".join(rect)

    def __repr__(self):
        """Return a string representation that can be used to recreate the object"""
        return "{:s}({:d}, {:d})".format(type(self).__name__, self.__width, self.__height)

    def __del__(self):
        """Destructor that is called when an instance is deleted"""
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute"""
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the larger rectangle after comparing"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
