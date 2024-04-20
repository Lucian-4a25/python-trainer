import sys
sys.path.append("..")

import time
import unittest

from project_1 import factorial, exponent, remove_min_max, variable_str_concat, split_str, defatul_param, count_substr, append_at_n, merge_list, is_palindrome, fibonacci, count_char, append_dict_keys, intersection, is_subset, remove_dict_keys

class TestProject1(unittest.TestCase):
    @unittest.skip("")
    def test_factorial(self):
     self.assertEqual(factorial(5), 120)


    @unittest.skip("")
    def test_exponent(self):
       self.assertEqual(exponent(5, 4), 625)
       self.assertEqual(exponent(2, 5), 32)

    
    @unittest.skip("")
    def test_remove_min_max(self):
      self.assertEqual(remove_min_max([1, 2, 5, 3, 4, 6, 7]), [2, 5, 3, 4, 6])
      self.assertEqual(remove_min_max([1, 22, 2, 12, 3, 4, 2, 3, 11, 2]), [2, 12, 3, 4, 2, 3, 11, 2])
    

    @unittest.skip("")
    def test_variable_str_concat(self):
       self.assertEqual(variable_str_concat("a", "b", "c"), "abc")
       self.assertEqual(variable_str_concat(), "")


    @unittest.skip("")
    def test_split_str(self):
      self.assertEqual(split_str("Emma-is-a-data-scientist"), ["Emma", "is", "a", "data", "scientist"])
    
    
    @unittest.skip("")
    def test_defatul_param(self):
       self.assertEqual(defatul_param(10), 10)
       self.assertEqual(defatul_param(10, 2), 20)


    @unittest.skip("")
    def test_count_substr(self):
      self.assertEqual(count_substr("David like eating apples, David is an actor", "David"), 2)
      self.assertEqual(count_substr("", "David"), 0)


    @unittest.skip("")
    def test_append_at_n(self):
      self.assertEqual(append_at_n("abc", "def", 1), "adefbc")
      self.assertEqual(append_at_n("abc", "def", 0), "defabc")
      self.assertEqual(append_at_n("abc", "def", 6), "abcdef")

    
    @unittest.skip("")
    def test_merge_list(self):
      self.assertEqual(merge_list([1, 2, 2, 3], [2, 3, 4, 5, 6, 6]), [1, 2, 3, 4, 5, 6])
      self.assertEqual(merge_list([1, 1, 2, 2, 3, 8, 9], [2, 2, 4, 5, 6, 6, 7, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    
    @unittest.skip("")
    def test_is_palindrome(self):
      self.assertEqual(is_palindrome(1), True)
      self.assertEqual(is_palindrome(111), True)
      self.assertEqual(is_palindrome(123), False)
      self.assertEqual(is_palindrome(335565533), True)
      
    @unittest.skip("")
    def test_fibonacci(self):
      self.assertEqual(fibonacci(0), 0)
      self.assertEqual(fibonacci(1), 1)
      self.assertEqual(fibonacci(2), 1)
      self.assertEqual(fibonacci(3), 2)
      self.assertEqual(fibonacci(10), 55)

    @unittest.skip("")
    def test_count_char(self):
      self.assertEqual(count_char("Apple"), {'A': 1, 'p': 2, 'l': 1, 'e': 1})

    @unittest.skip("")
    def test_append_dict_keys(self):
      self.assertEqual(append_dict_keys(["Jhon", "Tom"], {'Jhon':47, 'Emma':69 }), {'Jhon':48, 'Emma':69, 'Tom': 1 })

    @unittest.skip("")
    def test_remove_dict_keys(self):
      self.assertEqual(remove_dict_keys(["Jhon", "Tom"], {'Jhon':47, 'Emma':69 }), {'Emma':69 })

    @unittest.skip("")
    def test_intersection(self):
      start = time.time()
      mid = 100000
      left = range(1, mid)
      right = [mid - 1] * 50000
      vals = intersection(left, right)
      correct = [mid - 1]
      self.assertEqual(len(vals), len(correct))
      for v in vals:
        self.assertEqual(v in correct, True)
      end = time.time()
      self.assertTrue(end - start < 5)

    @unittest.skip("")
    def test_is_subset(self):
      max_val = 100000
      val = range(1, max_val + 1)
      start = time.time()
      self.assertEqual(is_subset(val, [max_val / 2] * 10000), True)
      val2 = [max_val / 2] * 50000
      val2.append( 2 * max_val)
      self.assertEqual(is_subset(val, val2), False)
      end = time.time()
      self.assertTrue(end- start < 5)