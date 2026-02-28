"""Tests de régression pour les 3 bogues logiques identifiés dans backend.operators."""

import unittest

from backend import operators


class TestOperatorLogicBugs(unittest.TestCase):
    """Couvre exactement les trois bogues ouverts en issues GitHub."""

    def test_bug_subtract_operand_order(self):
        """Bug #1: subtract(a, b) doit calculer a - b (et non b - a)."""
        self.assertEqual(operators.subtract(8, 3), 5)

    def test_bug_multiply_operator(self):
        """Bug #2: multiply(a, b) doit utiliser * (et non **)."""
        self.assertEqual(operators.multiply(4, 3), 12)

    def test_bug_divide_real_division(self):
        """Bug #3: divide(a, b) doit utiliser / (et non //)."""
        self.assertEqual(operators.divide(7, 2), 3.5)


if __name__ == "__main__":
    unittest.main()
