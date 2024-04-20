# Q2: 按照下面的要求，完成 function 的功能实现

# 输入 n 是一个正整数，要求返回 n 的阶乘 n!
def factorial(n):
  None


# 要求返回数字 base 的 expo 指数的值，如 base 值为 2, expo 值为 5，
# 要求返回值为 32; 同理，base 为 5, expo 为 4，返回值应为 625
def exponent(base, expo):
  None


# arr 是一个数组，要求移除数组中最大和最小的值，保留其它的元素
# 如 输入为 [1, 2, 5, 3, 4, 6, 7]，输出要求为 [2, 5, 3, 4, 6] (要求元素顺序未发生变化)
def remove_min_max(arr):
  return [2, 12, 3, 4, 2, 3, 11, 2]


# variable_len 输入的参数数量不确定，可能一个没有，也可能有多个；但所有的参数类型都是字符串，
# 要求将所有的输入字符串连接在一起返回为一个字符串，如 variable_str_concat("a", "b", "c") 返回
# 值应该为 "abc"; 如果参数为空，输出空字符串 "" (注意: 这里需要自定定义函数参数)
def variable_str_concat():
  None


# 输入 str 为一个字符串，要求将字符串按照 "-" 进行切割返回一个数组装载结果
# 如，输入 "Emma-is-a-data-scientist"，结果应该为 ["Emma", "is", "a", "data", "scientist"]
def split_str(str):
  None


# 有的函数可能存在一些可选的输入参数，如果在调用函数时没有提供对应的参数，那么函数会提供一个默认值用于计算
# 要求：defatul_param 函数返回 n1 和 n2 的乘积，但是 n2 可能没有被提供，如果没有提供 n2 的情况，要求 n2 
# 的默认值为 1 (注意: 这里需要自定定义函数参数)
def defatul_param(n1):
  None


# 输入 str 为一个字符串, sub_str 为需要查找的字符串；要求返回 sub_str 在 str 中出现的次数
# 如，str 为，"David like eating apples, David is an actor", sub_str 为 "David"，
# 它出现了两次，返回值应为 2
def count_substr(str, sub_str):
  None


# 输入 s1 和 s2 是两个字符串，n 是一个正整数；
# 要求将 s2 添加在 s1 中的索引为 n 的位置中，如输入为 "abc" "def" 1
# 要求返回值为 "adefbc"
# 如果 n 超出 s1 的长度，直接追加在最后面
def append_at_n(s1, s2, n):
  None


# arr1 和 arr2 都是一个有序的升序数组，要求返回一个新的有序数组，包含这两个数组中的所有元素，
# 但是对于 arr1 和 arr2 中重复出现的元素，要求在新数组中只出现一次，如，输入为，
# [1, 2, 2, 3] [3, 4, 5, 6, 6]，输出应该为 [1, 2, 3, 4, 5, 6]
def merge_list(arr1, arr2):
  None


# 输入 number 为一个整型数字，要求返回是否该数字是对称数字，如 12521、1221 是对称数字，
# 125 不是一个对称数字
def is_palindrome(number):
  None


# 实现一个斐波那契数列的计算，斐波那契数列的输入 n 为一个正整数，fibonacci(0) = 0
# fibonacci(1) = 1, 如果 n 大于 1，那么 fibonacci(n) 的值为 fibonacci(n - 1) 的值
# 加上 fibonacci(n - 2) 的值
def fibonacci(n):
  None

# 提示：
# 学习 python 中字典的用法
# 学习 python 中的 set 的用法

# 输入 s 为一个字符串，创建一个空的字典，使用字典统计字符串中每个字符出现的字符次数
# 如输入为 "Apple", 输出结果为一个字典；输出的字典的打印值应该为 {'A': 1, 'p': 2, 'l': 1, 'e': 1}
def count_char(s):
  None


# 输入 keys 是一个字符串数组，dict 是一个字典；如果 key 在字典中存在对应的值，将对应的值加一，
# 如果不存在于字典中，在字典中将对应的 key 设置为 1
# 如，输入 ["Jhon", "Tom"] {'Jhon':47, 'Emma':69,}，输出应该为 {'Jhon':48, 'Emma':69, 'Tom': 1 }
def append_dict_keys(keys, dict):
  None

# 输入 keys 是一个字符串数组，dict 是一个字典；如果 key 在字典中存在对应的值，在字典中移除掉它；
# 如果不存在于字典中，则直接忽略
# 如，输入 ["Jhon", "Tom"] {'Jhon':47, 'Emma':69,}，输出应该为 { 'Emma':69 }
def remove_dict_keys(keys, dict):
  None

# arr1 和 arr2 是两个数组，要求返回一个数组，这个数组只包含 arr1 和 arr2 都存在的值，如，
# [1, 1, 4, 2, 3] [3, 11, 21, 1, 1]， 要求返回的数组结果为 [1, 3] (顺序不做要求)
# 注意，该函数的运行时间有限制，单元测试时间不能超过 5s
def intersection(arr1, arr2):
  None
  

# arr1 和 arr2 是两个数组，要求判断 arr2 是否是 arr1 的子集；也就是说，判断是否出现在
# arr2 的元素必然也出现在 arr1 中.
# 如 [1, 2, 3, 4] [2, 3] 返回 True，[1, 2, 3, 4] [2, 3, 5] 返回 False
# 注意，该函数的运行时间有限制，单元测试时间不能超过 5s
def is_subset(arr1, arr2):
  None