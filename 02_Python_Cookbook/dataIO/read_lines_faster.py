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
Problem1:
    given a big data, larger than your memory, how to load it fast

Conclusion:
    Just use this, it is the built-in fastest way
    
    with open(fname, "r") as f:
        for lines in f.readlines():
            do something
"""

from __future__ import print_function
import time
import os

def example():
    with open("test.txt", "w") as f:
        f.write("\n".join(["abcdefghijklmnopqrstuvwxyz"]* 10000)) # 10000行
    fname = "test.txt"
    
    """ method 1 """
    with open(fname, "r") as f: # 3rd
        st = time.clock()
        while 1:
            lines = f.readlines(1000000)
            if not lines:
                break
            for line in lines:
                pass # do something
        print("method 1 takes: ",time.clock()-st)
    
    """ method 2 """
    with open(fname, "r") as f: # 2nd
        st = time.clock()
        for line in f:
            pass # do something
        print("method 2 takes: ", time.clock()-st)

    """ method 3 """
    with open(fname, "r") as f: # 1st
        st = time.clock()
        for line in f.readlines():
            pass # do something
        print("method 3 takes: ", time.clock()-st)
    
    os.remove("test.txt")
if __name__ == "__main__":
    example()