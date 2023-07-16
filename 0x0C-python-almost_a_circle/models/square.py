#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The identity of the square instance.

    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square. Default is 0.
            y (int, optional): The y-coordinate of the square. Default is 0.
            id (int, optional): The identity of the square instance. If None, the value is automatically generated.

        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns a string with information about this square.

        Returns:
            str: A string representation of the square.

        '''
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size property.

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        '''
        self.validate_integer("size", value, False)
        self.width = value
        self.height = value

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

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.

        Args:
            id (int, optional): The new identity value.
            size (int, optional): The new size value.
            x (int, optional): The new x-coordinate value.
            y (int, optional): The new y-coordinate value.

        '''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.

        If args is given, the attributes are updated in the order: id, size, x, y.
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
        '''Returns a dictionary representation of this square.

        Returns:
            dict: A dictionary containing the attributes of the square.

        '''
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
