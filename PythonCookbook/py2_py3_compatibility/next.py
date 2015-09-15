##encoding=utf8

"""
迭代方法的实现在python2和3中有不同的语法

在python2中是 def next(self)
在python3中是 def __next__(self)

请看下面的例子了解如何写出兼容2，3的迭代器
"""

from __future__ import print_function

def example1():
    """this is a python2 compatible only implementation"""
    class Upper(object):
        def __init__(self, iterable):
            self._iter = iter(iterable)
        def next(self):          # Py2-style, not working in Py3
            return self._iter.next().upper()
        def __iter__(self):
            return self
        
    for i in Upper("abcde"):
        print(i)
        
# example1()

def example2():
    """neat py2 py3 compatible implementation"""
    from builtins import object
    class Upper(object):
        def __init__(self, iterable):
            self._iter = iter(iterable)
        def __next__(self):      # Py3-style iterator interface
            return next(self._iter).upper()  # builtin next() function calls
        def __iter__(self):
            return self
        
    for i in Upper("abcde"):
        print(i)
    
# example2()

def example3():
    def generate():
        for i in [1,2,3,4,5]:
            yield i

    g = generate()
    print(next(g))


example3()