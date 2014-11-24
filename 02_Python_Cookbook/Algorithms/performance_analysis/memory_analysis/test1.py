##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

"""
there's no non ascii character is allowed if you
want to run memory_profiler in python3

test1:
    test memory use in if create and delete big list
    
test2:
    test memory use in if overwrite an existing object
"""

from memory_profiler import profile
import numpy as np

@profile
def test1():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

@profile
def test2():
    a = np.random.randn(1000, 1000)
    b = np.random.randn(1000, 1000)
    c = a * b
    d = np.dot(a, b)
    a = np.dot(a, b) # a is been overwritten, so doesn't cost much memory
    
if __name__ == '__main__':
    test1()
    test2()