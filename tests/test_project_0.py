import sys
sys.path.append("..")

import unittest

# print(sys.path)
from project_0 import even_or_odd, multiplication_or_sum

@unittest.skip("Skipping TestMultiplicationOrSum")
class TestMultiplicationOrSum(unittest.TestCase):
    def test_less_thousand(self):
        self.assertEqual(multiplication_or_sum(20, 50), 70)

    def test_more_thousand(self):
        self.assertEqual(multiplication_or_sum(10, 50), 500)

@unittest.skip("Skipping TestEvenOrOdd")
class TestEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_or_odd(2), 1)

    def test_odd(self):
        self.assertEqual(even_or_odd(1), 2)

    def test_non_num(self):
        self.assertEqual(even_or_odd("awdaw"), 0)
        self.assertEqual(even_or_odd(True), 0)


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestMultiplicationOrSum('test_less_thousand'))
    # suite.addTest(TestMultiplicationOrSum('test_more_thousand'))

    # # 创建测试运行器
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    unittest.main()
