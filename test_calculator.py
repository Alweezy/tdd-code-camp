from unittest import TestCase

from calculator import Calculator


class CalculatorTestCase(TestCase):
    """Test case suite for calculator class
    """

    def test_is_instance(self):
        """Test that oject is instance of calculator class"""
        result = Calculator(5, 7)

        self.assertIsInstance(result, Calculator,
                              msg="Should be an instance of class Sum")

    def test_input_integer(self):

        a = 'Name'
        b = 6

        addition = Calculator(a, b)
        self.result = addition.add_numbers()
        print(self.result)
        self.assertEqual(self.result, 'Inputs should be integers only!')

    def test_gets_sum(self):
        """Test that sum is actual"""

        self.a = 20
        self.b = 6
        addition = Calculator(self.a, self.b)
        result = addition.add_numbers()
        self.assertEqual(result, 26)
