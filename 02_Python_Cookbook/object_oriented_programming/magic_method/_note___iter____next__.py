##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
self.__iter__ 定义了 for i in self: 的行为
self.__next__ 定义了 next(self) 的行为 
"""

from __future__ import print_function

def example1():
    """对象本身的某一个属性是list, dict, set等默认可循环类。我们希望在
    for i in class 的时候是对这个属性作为循环。
    """
    class DictContainer(object):
        def __init__(self):
            self.data = dict()
        
        def __str__(self):
            return str(self.data)
        
        def __iter__(self):
            return iter(self.data) ## <== 直接对这个属性进行循环
        
    dc = DictContainer()
    dc.data = {1:"a", 2:"b"}
    print(dc)
    for i in dc: # 可以对其循环
        print(i)

# example1()

def example2():
    """在部分属性之间按照顺序进行循环
    """     
    class Cat(object):
        def __init__(self, name):
            self.name = name
            self.head = "cat_head"
            self.body = "cat_body"
            self.feet = "cat_feet"
            self.tail = "cat_tail"
            
        def __str__(self):
            return ("%s, %s, %s, %s, %s" % (self.name, self.head, self.body, self.feet, self.tail))
        
        def __iter__(self):
            iterable_attrs = [self.head, self.body, self.feet, self.tail] ## <== 定义可被循环到的属性
            return iter(iterable_attrs)

    cat = Cat("tom")
    print(cat)
    for i in cat:
        print(i)

# example2()

def example3():
    """
    用generator expression括号，和iter实现：
        对待字典中的key，有选择的迭代
    """
    class Myclass():
        def __init__(self):
            self.data = dict()
            
        def __iter__(self):
            return (key for key in self.data if key != "special")
        
    mc = Myclass()
    mc.data = {"a": 3, "b":1, "c":2, "special":0}
    for key in mc:
        print(key)
        
# example3()

def example4():
    """
    stackoverflow上面看来的一个recipe
    """
    class Myclass():
        def __init__(self):
            self.data = dict()
            self.current = 1
            
        def __iter__(self):
            return self
        
        def next(self):
            key = [k for k, v in self.data.items() if v == self.current]
            if not key:
                raise StopIteration
            self.current += 1
            return next(iter(key))
        
    mc = Myclass()
    mc.data = {"a": 3, "b":1, "c":2, "d":4, "e": 2}
    for key in mc:
        print(key)
        
# example4()

def example5():
    """python3 only
    """
    class Fib(object):
        def __init__(self, max):
            self.max = max
            
        def __iter__(self):
            self.a = 0
            self.b = 1
            return self
        
        def __next__(self):
            fib = self.a
            if fib > self.max:
                raise StopIteration
            self.a, self.b = self.b, self.a + self.b
            return fib
    
    fib = Fib(10)
    for i in fib:
        print(i)
        
example5()