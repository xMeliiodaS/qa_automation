import unittest
from math_function import is_even
from math_function import modulo_function
from math_function import sum_function
from math_function import sub_function
from math_function import mul_function
from math_function import div_function


class TestMathFunction(unittest.TestCase):

    def test_is_even_true(self):
        # Arrange
        num = 4  # Mock

        # Act
        result = is_even(num)

        # Assert
        self.assertTrue(result)

    # Coverage - I did unit test for the True result. So also I should do for the False result.
    def test_is_even_false(self):
        # Arrange
        num = 3  # Mock

        # Act
        result = is_even(num)

        # Assert
        self.assertFalse(result)

    def test_modulo_function_zero(self):
        self.assertEqual(0, modulo_function(4), "The function not working well.")
        # self.assertEqual(Expected, Actual, msg)

    # Unit test for the sum function with coverage --------------------------------
    def test_sum_function_positive_numbers(self):
        self.assertEqual(10, sum_function(4, 6))

    def test_sum_function_negative_numbers(self):
        self.assertEqual(sum_function(-1, -2), -3)

    def test_sum_function_mixed_numbers(self):
        self.assertEqual(sum_function(-1, 1), 0)

    def test_sum_function_zero(self):
        self.assertEqual(sum_function(0, 0), 0)

    def test_sum_function_str(self):
        self.assertFalse(sum_function(4, 2), "6")

    # Unit test for the subtract function with coverage --------------------------------
    def test_sub_function_positive_numbers(self):
        self.assertEqual(8, sub_function(3, 5))

    def test_sub_function_negative_numbers(self):
        self.assertEqual(-10, sub_function(-15, -5))

    def test_sub_function_mixed_numbers(self):
        self.assertEqual(-10, sub_function(-5, 5))

    def test_sub_function_zero(self):
        self.assertEqual(0, sub_function(0, 0))

    # Unit test for the multiply function with coverage --------------------------------
    def test_mul_function_positive_numbers(self):
        self.assertEqual(24, mul_function(4, 6))

    def test_mul_function_negative_numbers(self):
        self.assertEqual(24, mul_function(-4, -6))

    def test_mul_function_mixed_numbers(self):
        self.assertEqual(-24, mul_function(-4, 6))

    def test_mul_function_zero(self):
        self.assertEqual(0, mul_function(0, 0))

    # Unit test for the division function with coverage --------------------------------
    def test_div_function_positive_numbers(self):
        self.assertEqual(5, div_function(15, 3))

    def test_div_function_negative_numbers(self):
        self.assertEqual(3, div_function(-15, -5))

    def test_div_function_mixed_numbers(self):
        self.assertEqual(-2, div_function(10, -5))

    def test_div_numerator_zero(self):
        self.assertEqual(0, div_function(0, 5))

    def test_div_function_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_function(5, 0)


if __name__ == '__main__':
    unittest.main()
