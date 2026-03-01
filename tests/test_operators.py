"""Unit tests for core arithmetic behavior in backend.operators."""

import unittest

from backend import operators


class TestOperatorLogicBugs(unittest.TestCase):
    def test_subtract_operand_order(self):
        """Checks that subtraction follows standard operand order."""
        self.assertEqual(operators.subtract(8, 3), 5)

    def test_multiply_returns_product(self):
        """Checks that multiplication returns the arithmetic product."""
        self.assertEqual(operators.multiply(4, 3), 12)

    def test_divide_returns_real_result(self):
        """Checks that division returns the expected real-number result."""
        self.assertEqual(operators.divide(7, 2), 3.5)


if __name__ == "__main__":
    unittest.main()
