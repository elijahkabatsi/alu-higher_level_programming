#!/usr/bin/python3
"""Defines class BaseGeometry with area method."""


class BaseGeometry:
    """BaseGeometry with unimplemented area method."""

    def area(self):
        """Raise exception for unimplemented area."""
        raise Exception("area() is not implemented")
