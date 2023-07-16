#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The identity of the rectangle instance.

    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Default is 0.
            y (int, optional): The y-coordinate of the rectangle. Default is 0.
            id (int, optional): The identity of the rectangle instance. If None, the value is automatically generated.

        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width property.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        '''
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height property.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        '''
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x-coordinate of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x property.

        Args:
            value (int): The x-coordinate value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        '''
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y-coordinate of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y property.

        Args:
            value (int): The y-coordinate value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        '''
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.

        Args:
            name (str): The name of the attribute being validated.
            value (int): The value to be validated.
            eq (bool, optional): If True, the value must be greater than or equal to 0. If False, the value must be greater than 0. Default is True.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value does not meet the specified condition.

        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Compute the area of this rectangle.

        Returns:
            int: The area of the rectangle.

        '''
        return self.width * self.height

    def display(self):
        '''Prints a string representation of this rectangle.

        The rectangle is drawn using the '#' character.

        '''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Returns a string with information about this rectangle.

        Returns:
            str: A string representation of the rectangle.

        '''
        return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.

        Args:
            id (int, optional): The new identity value.
            width (int, optional): The new width value.
            height (int, optional): The new height value.
            x (int, optional): The new x-coordinate value.
            y (int, optional): The new y-coordinate value.

        '''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.

        If args is given, the attributes are updated in the order: id, width, height, x, y.
        If kwargs is given, the attributes are updated based on the key-value pairs.

        Args:
            *args (list): List of values to update the attributes.
            **kwargs (dict): Dictionary with key-value pairs to update the attributes.

        '''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns a dictionary representation of this rectangle.

        Returns:
            dict: A dictionary containing the attributes of the rectangle.

        '''
        return {"id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y}
