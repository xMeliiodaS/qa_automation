import unittest

from math_function import is_even
from math_function import modulo_function


class TestMathFunction(unittest.TestCase):

    def test_is_even_true(self):
        num = 4  # Mock
        result = is_even(num)
        self.assertTrue(result)

    def test_modulo_function_zero(self):
        self.assertEqual(0, modulo_function(4), "The function not working well.")
        # Expected, Actual
