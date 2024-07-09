#!/usr/bin/python3
"""
Define a class MyList that inherits from list.
"""

class MyList(list):
    """
    A custom list class inheriting from Python's built-in list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
