##encoding=UTF8

"""
Python代码的标准测试框架

首先我们来问自己几个问题:
    1. 如何确认一个函数工作正常? 对于一些特殊例子是否也能工作正常?
    2. 如果一个函数被修改之后, 怎么快速的验证他工作正常?
    3. 如果由另一个开发者来修改代码, 怎么确保他能够修改后的代码还能工作正常?

由于我们在编写代码的时候通常都是问题导向的。我们不断的尝试, 直到代码给出我们所期待的输出。但是在这个
过程中我们并不可能对所有可能的输入进行测试, 所以我们必须要有一套科学的测试方法来测试我们的代码。

Python标准库中的unittest框架的测试流程大致可以描述如下:
对你所要解决的问题, 中间有几个类, 方法和函数。首先我们模拟一个问题的输入, 这个输入可以用:
self.setUp() 和 self.setUpClass() 来预先准备好。然后针对我们每个要测试的单元, 写一个函数。
然后用内置的assert系列函数来验证我们的输出是否和我们预期的结果一致即可。

reference = https://docs.python.org/2/library/unittest.html#classes-and-functions
"""


from __future__ import print_function
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()