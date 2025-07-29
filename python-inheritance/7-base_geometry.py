#!/usr/bin/python3
"""Defines BaseGeometry with area and integer validation."""


class BaseGeometry:
    """BaseGeometry with validation and area placeholder."""

    def area(self):
        """Raise exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
