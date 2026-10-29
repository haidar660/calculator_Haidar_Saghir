"""Unit tests for all calculator operations."""

import unittest

from calculator_Haidar_Saghir import (
    add,
    divide,
    modulus,
    multiply,
    power,
    square_root,
    subtract,
)


class TestCalculator(unittest.TestCase):
    """Verify the basic and extended calculator functions."""

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_modulus_by_zero(self):
        with self.assertRaisesRegex(ValueError, "modulus with zero"):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 5), 32)

    def test_power_with_negative_exponent(self):
        self.assertEqual(power(2, -2), 0.25)

    def test_square_root(self):
        self.assertEqual(square_root(81), 9)

    def test_square_root_of_negative_number(self):
        with self.assertRaisesRegex(ValueError, "negative number"):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
