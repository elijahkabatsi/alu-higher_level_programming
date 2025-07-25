#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class that supports printing sorted version."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (without modifying the original)."""
        print(sorted(self))
