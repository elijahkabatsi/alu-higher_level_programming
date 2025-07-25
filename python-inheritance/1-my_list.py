#!/usr/bin/python3
"""Custom list class with sorted print."""


class MyList(list):
    """Inherits from list and adds print_sorted method."""

    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        print(sorted(self))
