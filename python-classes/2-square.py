#!/usr/bin/python3
"""Defines a class Square with size validation."""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize the square with validated size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
