##encoding=utf-8

"""
程序设计中有这样一种需求:

class MyClass
    def method
    
    def option1
    
    def option2
    
    ...
    
我们对同样的一个输入, 可能要根据情况判断使用option1, option2, ...
对此我们有两种做法:

1. if: ..., option1, elif: ..., option2, ...
    这种做法适用于每一个output的情况都可能不一样, 所以每次都需要做判断
2. if: ..., method = option, elif ..., method = option2, ... 然后以后都调用method方法
    这种做法适用于很多个input的情况都一样, 所以我们可以显式的将method绑定到option1, option2上。
    以后如果发现method不适用目前的input, 那么我们可以用try: except: 捕获, 然后重新检查一次, 并
    绑定方法。
    
    
我们来测试一下性能吧
"""

import time

class SQLEngine():
    def __init__(self):
        self.auto_commit = True
        self.commit = self.commit_true
        
    def commit_true(self):
        pass
    
    def commit_false(self):
        pass
    
    def autocommit(self, flag):
        if flag:
            self.commit = self.commit_true
        else:
            self.commit = self.commit_false
            
    def insert1(self, record):
        """do if check everytime
        """
        if self.auto_commit:
            self.commit_true()
    
    def insert2(self, record):
        """use commit(), change the binding when needed
        """
        self.commit()
        
complexity = 1000000
engine = SQLEngine()

st = time.clock()
for i in range(complexity):
    engine.insert1(i)
print(time.clock() - st)
            
st = time.clock()
for i in range(complexity):
    engine.insert2(i)
print(time.clock() - st)