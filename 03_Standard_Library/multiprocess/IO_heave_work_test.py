##encoding=utf8

"""
given 1000 files, count total character in these 1000 files
"""

from multiprocessing import Pool
import time
import os

def totalchar(foldername):
    counter = 0
    for fname in os.listdir(foldername):
        with open(os.path.join(foldername, fname), "r") as f:
            for line in f.xreadlines():
                counter += len(line.strip())
                
    return counter

if __name__ == '__main__':
    ## 单进程方法
    st = time.clock()
    print(totalchar("a1"))
    print(totalchar("a2"))
    print(time.clock() - st)
    
    ## 多进程方法    
    st = time.clock()
    pool = Pool()
    print pool.map(totalchar, ["a1", "a2"])
    print(time.clock() - st