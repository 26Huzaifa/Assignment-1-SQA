import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_exponent(self):
        self.assertEqual(calculator.exponent(2, 3), 8)
        self.assertEqual(calculator.exponent(1, 3), 1)
        self.assertEqual(calculator.exponent(-2, 3), -8)
        self.assertEqual(calculator.exponent(-2, 4), 16)
        self.assertEqual(calculator.exponent(4, -1), 0.25)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(1, 4), 0.25)
        self.assertEqual(calculator.divide(7, 0), None)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 5), 10)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(-2, -5), 10)

    def test_add(self):
        self.assertEqual(calculator.add(7, 3), 10)
        self.assertEqual(calculator.add(-7, 3), -4)
        self.assertEqual(calculator.add(-7, -3), -10)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(7, 2), 5)
        self.assertEqual(calculator.subtract(-7, 2), -9)
        self.assertEqual(calculator.subtract(-7, -2), -5)


if __name__ == '__main__':
    unittest.main()
