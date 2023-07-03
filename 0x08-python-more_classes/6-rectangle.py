#!/usr/bin/python3

"""Define a Rectangle"""

class Rectangle:
    """Rectangle class"""
    number_of_instances = 0  # Class attribute to keep track of the number of instances created

    def __init__(self, width=0, height=0):
        """Initialize width and height attributes"""
        self.width = width  # Initialize width attribute
        self.height = height  # Initialize height attribute
        Rectangle.number_of_instances += 1  # Increment the number of instances

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""  # Return an empty string if width or height is 0

        size = "#" * self.__width  # Create a string of "#" with a length equal to width
        rect = []
        for index in range(self.__height):
            rect.append(size)  # Add the width string to the rectangle list for each height
        return "\n".join(rect)  # Join the strings in the rectangle list with newline characters

    def __repr__(self):
        """Return a string representation that can be used to recreate the object"""
        return "{:s}({:d}, {:d})".format((type(self).__name__), self.__width, self.__height)

    def __del__(self):
        """Destructor method that is called when the object is about to be destroyed"""
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
        print("Bye rectangle...")  # Print a message when the object is destroyed

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")  # Raise an error if width is not an integer
        if value < 0:
            raise ValueError("width must be >= 0")  # Raise an error if width is less than 0
        self.__width = value  # Set the width attribute

    @property
    def height(self):
        """Getter method for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")  # Raise an error if height is not an integer
        if value < 0:
            raise ValueError("height must be >= 0")  # Raise an error if height is less than 0
        self.__height = value  # Set the height attribute

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return None  # Return None if width or height is 0
        return (self.__height * 2) + (self.__width * 2)
