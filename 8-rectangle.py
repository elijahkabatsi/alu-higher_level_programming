#!/usr/bin/python3
"""Defines Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle using BaseGeometry integer validation"""

    def __init__(self, width, height):
        """Initialize with width and height (validated)"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
