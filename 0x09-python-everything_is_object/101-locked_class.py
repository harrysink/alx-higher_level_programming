#!/usr/bin/python3
"""Module 101-locked_class
Defines a LockedClass class.
"""


class LockedClass:

    __slots__ = ['first_name']
    """Prevents the declaration of any variable
    that isn't in __slots__
    """

    def __init__(self, first_name=''):
        """Initializes a LockedClass instance

        Args:
            first_name: first_name of individual
        """
        self.first_name = first_name
