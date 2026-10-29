"""Basic calculator operations for the Lab 6 PyBuilder project."""

import math


def add(x, y):
    """Return the sum of two numbers."""
    return x + y


def subtract(x, y):
    """Return the difference between two numbers."""
    return x - y


def multiply(x, y):
    """Return the product of two numbers."""
    return x * y


def divide(x, y):
    """Return x divided by y.

    Raises:
        ValueError: If y is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def modulus(x, y):
    """Return the remainder after dividing x by y.

    Raises:
        ValueError: If y is zero.
    """
    if y == 0:
        raise ValueError("Cannot calculate modulus with zero.")
    return x % y


def power(base, exponent):
    """Return base raised to exponent."""
    return base**exponent


def square_root(value):
    """Return the square root of a non-negative number.

    Raises:
        ValueError: If value is negative.
    """
    if value < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(value)
