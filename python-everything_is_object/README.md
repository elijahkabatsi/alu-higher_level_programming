# Python - Inheritance

This project explores the concept of **inheritance** in Python — one of the fundamental principles of object-oriented programming (OOP). Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class), promoting code reuse and logical hierarchy.

## Learning Objectives

By the end of this project, you will be able to:

- Understand the basics of inheritance in Python
- Use the `dir()` function to retrieve attributes and methods of an object
- Distinguish between base classes and subclasses
- Override parent methods in child classes
- Use the `super()` function to call parent class methods
- Understand how to inspect class relationships with `issubclass()` and `isinstance()`

## File Descriptions

| File            | Description |
|-----------------|-------------|
| `0-lookup.py`   | Contains a function `lookup(obj)` that returns a list of all attributes and methods of an object. |
| `0-main.py`     | Test file to verify the behavior of `lookup()` with different classes. |

## Example Usage

```python
class MyClass:
    my_attr = 42
    def my_method(self):
        return "Hello"

print(lookup(MyClass))
# Output: ['__class__', ..., 'my_attr', 'my_method']
