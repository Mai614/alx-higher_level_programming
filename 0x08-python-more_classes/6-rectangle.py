#!/usr/bin/python3

class Rectangle:
    """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize width and height attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Return a string representation that can be used to recreate the object"""
        return "{:s}({:d}, {:d})".format((type(self).__name__), self.__width, self.__height)

    def __del__(self):
        """Destructor method that is called when the object is about to be destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute"""
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
            return None
        return (self.__height * 2) + (self.__width * 2)
