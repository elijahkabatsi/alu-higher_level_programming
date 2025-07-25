#!/usr/bin/python3
"""Custom list class with sorted print."""

class MyList(list):
    def print_sorted(self):
        print(sorted(self))
