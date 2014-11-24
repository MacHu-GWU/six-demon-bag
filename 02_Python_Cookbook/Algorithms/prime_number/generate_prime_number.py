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
Fastest algorithm to generate all prime number from 1-n
"""

from __future__ import print_function
import numpy as np
import math
import time

n = 100000

def prime1(upto):
    """for i in 2 到 upto，尝试用 2 到 sqrt(i) 的因子筛选i
    
    注意：用filter返回在py2和py3中有不同的结果。在2中是返回
    实际的可循环对象，在3中是返回filter后的元素的指针。在应用
    中最好还是不要直接返回filter。具体原因请参考：
    python27-easy-doc/02_python_cookbook/built-in_function/_note_map_reduce_filter.py
    """
    return filter(lambda num: (
                               num % np.arange(2,
                                               1+int(math.sqrt(num))
                                               ) 
                               ).all(), 
                  range(2,upto+1))

st = time.clock()                  
prime1(n)
print("%.8f" % (time.clock() - st))

def prime2(upto):
    """方法同prime1。只不过使用了list数据结构作为容器。
    使用列表推导得到列表后再转化为numpy，而不是直接用numpy.ndarray计算
    """
    return filter(lambda num: np.array( # 最后将列表放入np.array
                                       [num % factor for factor in range(2,
                                                                         1+int(math.sqrt(num))
                                                                         )]
                                       ).all(), 
                  range(2,upto+1))

# st = time.clock()                  
# prime2(n)
# print("%.8f" % (time.clock() - st))

def prime3(upto):
    """方法同prime1。只不过筛选时排除掉了偶数
    """
    return [2] + filter(lambda num: (
                                     num % np.arange(3,
                                                        1+int(math.sqrt(num)),
                                                        2) # 排除掉了偶数
                                     ).all(), 
                        range(3,upto+1,2))
                      
# st = time.clock()                  
# prime3(n)
# print("%.8f" % (time.clock() - st))

def prime4(upto):
    """
    """
    primes=[2]
    for num in range(3,upto+1,2):
        isprime=True
        for factor in range(3,1+int(math.sqrt(num)),2):
            if not num % factor: 
                isprime=False
                break
        if isprime: 
            primes.append(num)    
    return primes

st = time.clock()                  
prime4(n)
print("%.8f" % (time.clock() - st))

def prime5(upto):
    """动态规划解法+numpy指针列表数据容器
    返回的是numpy.array
    """
    primes=np.arange(2,upto+1)
    isprime=np.ones(upto-1,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[factor-2]: 
            isprime[factor*2-2::factor]=0
    return primes[isprime]

st = time.clock()                  
prime5(100000)
print("%.8f" % (time.clock() - st))