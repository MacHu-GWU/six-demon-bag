##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

from __future__ import print_function
import numpy as np
from scipy import stats
from scipy.stats import norm

def example1():
    """正态分布函数
    """
    print('bounds of distribution lower: %s, upper: %s' % (norm.a,norm.b) )
    print(norm.cdf(0) )
    print(norm.pdf(0) )
    
example1()

def example2():
#     dist_continu = [d for d in dir(stats) if
#                     isinstance(getattr(stats,d), stats.rv_continuous)]
#     print(dist_continu)
    print(stats.rv_continuous.__doc__)
    
example2()