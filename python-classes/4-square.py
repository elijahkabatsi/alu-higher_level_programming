#!/usr/bin/python3
"""Defines a class Square with encapsulated size and area computation."""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize the square with a validated size"""
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with type and value checks"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return self.__size * self.__size
