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
# from memory_profiler import profile
from collections import defaultdict
import numpy as np
import math
import time

# def prime(upto):
#     """动态规划解法+numpy指针列表数据容器
#     返回的是numpy.array
#     """
#     primes=np.arange(2,upto+1)
#     isprime=np.ones(upto-1,dtype=bool)
#     for factor in primes[:int(math.sqrt(upto))]:
#         if isprime[factor-2]: 
#             isprime[factor*2-2::factor]=0
#     return primes[isprime]
# 
# def pfac(num):
#     d=defaultdict(int)
#     for f in prime(int(math.sqrt(num) ) ):
#         d[f]+=1
# 
#     terms=[]
#     for e in sorted(d.keys()):
#         if d[e]>1:
#             terms.append('{:,}^{}'.format(e,d[e]))
#         else:
#             terms.append('{:,}'.format(e))
# 
#     print(' * '.join(terms),'=','{:,}'.format(num)  )
#     
# pfac(24)

# @profile
def factor(n):
    res = list()
    i = 2
    limit = math.sqrt(n)    
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n = n / i
            limit = math.sqrt(n)   
        else:
            i += 1
    if n > 1:
        res.append(n)
    return res


st = time.clock()
print(factor(600851475143*1000000+1))
print("%.8f" % (time.clock() - st))
    
