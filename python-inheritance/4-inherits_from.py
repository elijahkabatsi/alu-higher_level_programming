#!/usr/bin/python3
"""Defines a function to check inherited class relationships."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (not same class)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
