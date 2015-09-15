##encoding=utf-8

from __future__ import print_function
import timeit

def basic_usage():
    print( timeit.timeit('"-".join(str(n) for n in range(100))', number=10000) )
    print( timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000) )
    print( timeit.timeit('"-".join(map(str, range(100)))', number=10000) )
    
# basic_usage()

def measure_a_function():
    def func():
        counter = 0
        for i in range(1000000):
            counter += i
    
    howmany = 100
    # 用timeit重复若干次, 然后除以次数
    print( timeit.timeit(func, number=howmany)/howmany )
    
    # 用repeat重复若干次, 每次运行一次, 然后对时间列表求平均
    print( sum(timeit.repeat(func, repeat=howmany, number=1))/howmany )
    
# measure_a_function()