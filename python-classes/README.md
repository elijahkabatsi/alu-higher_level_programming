# Python - Classes and Objects

This directory contains Python scripts that demonstrate the concept of classes and objects in Python. It is part of the ALU Higher Level Programming curriculum.

## Task: 0. My first square

**File:** `0-square.py`

This script defines an **empty class** named `Square`. It is the starting point for understanding how classes are created in Python.

### Requirements

- The class must be named `Square`.
- It must be an empty class (use the `pass` statement).
- You are **not allowed to import any module**.
- The class should have a docstring, and follow Python coding style guidelines (PEP8).

### Example Usage

```bash
$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
