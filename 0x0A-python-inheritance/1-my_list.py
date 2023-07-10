#!/usr/bin/python3

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    This class adds a method to print the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        This method sorts the elements of the list in ascending order and
        prints them.
        """
        print(sorted(self))
