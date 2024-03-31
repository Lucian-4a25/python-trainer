import sys
sys.path.append("..")

import unittest

# print(sys.path)
from project_0 import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_or_odd(2), 1)

    def test_odd(self):
        self.assertEqual(even_or_odd(1), 2)

    def test_non_num(self):
        self.assertEqual(even_or_odd("awdaw"), 0)
        self.assertEqual(even_or_odd(True), 0)


if __name__ == '__main__':
    unittest.TestCase
