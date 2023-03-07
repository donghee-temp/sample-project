import unittest

import sample

class TestSample(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(sample.fibonacci(0), 0)
        self.assertEqual(sample.fibonacci(1), 1)
        self.assertEqual(sample.fibonacci(2), 1)
        self.assertEqual(sample.fibonacci(3), 2)
        self.assertEqual(sample.fibonacci(4), 3)
        self.assertEqual(sample.fibonacci(9), 34)

    def test_factorial(self):
        self.assertEqual(sample.factorial(1), 1)
        self.assertEqual(sample.factorial(2), 2)
        self.assertEqual(sample.factorial(3), 6)
        self.assertEqual(sample.factorial(4), 24)
        self.assertEqual(sample.factorial(5), 120)


if __name__ == '__main__':
    unittest.main()
