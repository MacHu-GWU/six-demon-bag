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
there's no non ascii character is allowed if you
want to run memory_profiler in python3

test memory use in sanhe made quick sort and system built-in sort method
"""

import random
import copy

@profile
def qsort(L):
    """3 line python quick sort"""
    if len(L) <= 1: 
        return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + qsort([ge for ge in L[1:] if ge >= L[0]]) 

@profile
def builtin_sort(L):
    """built-in sort() method"""
    L = copy.copy(L)
    L.sort()
    return L

if __name__ == '__main__':
    L = [i for i in range(1,10000)]
    random.shuffle(L)
    sorted_L = qsort(L)
    sorted_L = builtin_sort(L)