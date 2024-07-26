import unittest

from basic_operators.first import add, divide, multiply, reminder, subtract
from basic_operators.second import (check_if_bigger, check_if_equal,
                                    check_if_smaller)


class TestArithmeticOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_reminder(self):
        self.assertEqual(reminder(10, 3), 1)
        self.assertEqual(reminder(-10, 3), -1)
        self.assertEqual(reminder(-10, -3), -1)
        with self.assertRaises(ValueError):
            reminder(10, 0)


class TestComparisonOperations(unittest.TestCase):

    def test_check_if_bigger(self):
        self.assertTrue(check_if_bigger(10, 5))
        self.assertFalse(check_if_bigger(5, 10))
        self.assertFalse(check_if_bigger(5, 5))

    def test_check_if_smaller(self):
        self.assertTrue(check_if_smaller(5, 10))
        self.assertFalse(check_if_smaller(10, 5))
        self.assertFalse(check_if_smaller(5, 5))

    def test_check_if_equal(self):
        self.assertTrue(check_if_equal(5, 5))
        self.assertFalse(check_if_equal(10, 5))
        self.assertFalse(check_if_equal(5, 10))


if __name__ == "__main__":
    unittest.main()
