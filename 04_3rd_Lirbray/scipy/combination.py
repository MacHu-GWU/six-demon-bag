
##coding=utf8
# 计算排列组合
import time
import scipy.misc as sc

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

import math
def choose2(n, k):
    '''Brute method to find factorial'''
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

n, k = 500,188
st = time.clock()
print choose(n, k)
print time.clock() - st

st = time.clock()
print choose2(n, k)
print time.clock() - st

st = time.clock()
print sc.comb(n, k, exact=True)
print time.clock()-st

