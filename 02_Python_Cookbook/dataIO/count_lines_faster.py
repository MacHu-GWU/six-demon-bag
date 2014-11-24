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
[EN]
Problem:
    Given a big text file, which is the best way to count how many line in the file.
    
Conclusion:
    Use buffer. Even the size larger than your memory, this method still working.
    
[CN]
问题：如何快速计算有文件有多少行
结论：用缓冲内存，计算换行符的个数
"""

from __future__ import print_function
import time
import os

def get_file_lines(fname):
    """ generator method, yield, enumerate"""
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_file_lines1(fname):
    """ built-in loop method in file object """
    with open(fname) as f:
        i = 0
        for line in f:
            i += 1
            pass
        return i
            
def get_file_lines2(fname): ## BEST method with low memory consum
    """ count "\n" using buffer method """
    def block(file, size = 65500):
        """ load data using buffer """
        while 1:
            chunk = file.read(size)
            if not chunk: ## nb not None, then, not nb = False
                break
            yield chunk
    with open(fname, "r") as f:
        return sum(line.count("\n") for line in block(f)) + 1

def get_file_lines3(fname):
    return sum(1 for line in open(fname))

def get_file_lines4(fname):
    with open(fname, "r") as f:
        return f.read().count("\n") + 1
    

if __name__ == "__main__":
    def performance_test():
        with open("test.txt", "w") as f:
            f.write("\n".join(["abcdefghijklmnopqrstuvwxyz"]* 10000)) # 10000行
        
        n = 100 ## iterate time
        fname = "test.txt" ## put a text file under same folder
        t1,t2,t3,t4,t5 = 0,0,0,0,0
        for ii in range(n):    
            """ test1 """
            st = time.clock()
            i = get_file_lines(fname) ## 3rd
            t1 += time.clock() - st
#             print(i)  
            
            """ test2 """
            st = time.clock()
            i = get_file_lines1(fname) ## 4th
            t2 += time.clock() - st
#             print(i)
            
            """ test3 """
            st = time.clock()
            i = get_file_lines2(fname) ## 1st
            t3 += time.clock() - st
#             print(i)
            
            """ test4 """
            st = time.clock()
            i = get_file_lines3(fname) ## 5th
            t4 += time.clock() - st
#             print(i)
            
            """ test5 """
            st = time.clock()
            i = get_file_lines4(fname) ## 2nd
            t5 += time.clock() - st
#             print(i)
            
        print("%s, %s, %s, %s, %s" % (t1, t2, t3, t4, t5))
        os.remove(fname)
    performance_test()