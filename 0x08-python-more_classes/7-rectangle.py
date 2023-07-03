#!/usr/bin/python3

class Rectangle:
    
    # Class attribute to keep track of the number of instances created
    number_of_instances = 0
    
    # Class attribute to specify the symbol used for printing the rectangle
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor method for Rectangle class.

        Args:
            width (int): Width of the rectangle (default is 0)
            height (int): Height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height
        
        # Increment the number of instances
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        String representation of the Rectangle object.

        """
        if self.__height == 0 or self.__width == 0:
            return ""
        
        size = str(self.print_symbol) * self.__width
        rect = []
        for index in range(self.__height):
            rect.append(size)
        
        return "\n".join(rect)

    def __repr__(self):
        """
        String representation of the Rectangle object.

        """
        return "{:s}({:d}, {:d})".format((type(self).__name__), self.__width, self.__height)

    def __del__(self):
        """
        Destructor method for Rectangle class.
        
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Getter method for the width attribute.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The value to set as the width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The value to set as the height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        """
        if self.__height == 0 or self.__width == 0:
            return 0
