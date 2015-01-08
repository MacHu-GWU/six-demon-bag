##encoding=utf8

"""
Parse第三方库可以实现与str.format()相反的功能

例如有一个字符串 "name=sanhe, age=12", 我们只需要定义 "name={}, age={}", 我们就可以从字符串中解析出
我们需要的内容

res = https://pypi.python.org/pypi/parse
"""

from __future__ import print_function
from parse import parse, search, compile

def example1():
    """parse method
    """
    res = parse("name={}, age={}", "name=sanhe, age=12")
    print(res, type(res))
    name, age = res # 可以使用tuple assignment表达式
    print(name, age)
    name, age = res[0], res[1] # 也可以使用list[index]表达式
    
# example1()

def example2():
    """search method
    """
    res = search("Age: {:d}\n", "Name: Rufus\nAge: 42\nColor: red\n")
    print(res)
    
# example2()

def example3():
    """compile method
    """
    p = compile("name={}, age={}")
    res = p.parse("name=sanhe, age=12")
    print(",".join(res))
    
# example3()

def example4():
    """parse string to different field
    """
    res = parse("name={name}, age={age}", "name=sanhe, age=12")
    print(res)
    
# example4()