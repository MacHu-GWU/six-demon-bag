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

from __future__ import print_function
import os
import time
import pprint


"""
dict.fromkeys is a very fast way to initial a dict that all keys map to the same value.
!!! WARNING, becareful to work with mutable objects though:
"""
def example1():
    """由于data[1], data[2], data[3]都指向同一个字典{"a": -1, "b": -1, "c": -1}
    当修改data[1]指向另一个对象的时候，这样并不会对data[2], data[3]造成影响
    """
    a, b = [1,2,3], ["a", "b", "c"]
    data1 = dict.fromkeys(a, dict.fromkeys(b, -1) )
    data2 = dict.fromkeys(a, dict.fromkeys(b, -1) )
    print("=== data1 Before ===")
    pprint.pprint( data1 )
    print("=== data1 After data[1] = [11, 22, 33]===")
    data1[1] = [11,22,33] 
    pprint.pprint( data1 )
    """可当对data[1]中的字典进行操作时，例如 data[1]["a"] = 999，那么data其他的key
    也会指向这个被修改过的字典，所以会造成影响。所以，只要对所有key指向的那个对象本身进行操作
    所有key指向的对象就都会被改变。
    """
    print("=== data2 Before ===")
    pprint.pprint( data2 )
    print("=== data2 After data[1]['a'] = 999===")
    
    data2[1]["a"] = 999 ## <== 会把 data[1]["a"], data[2]["a"], data[3]["a"] 都改过来
    pprint.pprint( data2 )  
    
# example1()

def example2():
    n = 1000000
    
    a, b = list(), list()
    for i in xrange(n):
        a.append(i)
        b.append(os.urandom(32))
        
    st = time.clock()
    data = { key : -1 for key in a}
    print("python generate expression time elapse = %s" % (time.clock() - st,) )
    
    st = time.clock()
    data = dict.fromkeys(a, -1)
    print("built-in method time elapse = %s" % (time.clock() - st,) )
    print("结论：速度是差不了多少的， dict.fromkey略快")

# example2()

def example3():
    data = { k: k+1 for k in range(10)  }
    print(data)
    
# example3()