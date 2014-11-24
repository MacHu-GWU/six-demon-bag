##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-15             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
如何用获得一个任意大文件的md5验证码？
我们首先要一小部分一小部分的用二进制读取文件，
这样避免了一次性把文件dump到内存中。
然后由于md5可以增量update，所以我们可以一个一个
的处理chunk。实例程序如下：
"""
from __future__ import print_function
import hashlib
import time
import os
import sys

def create_testfile(text):
    with open("test_file.txt", "w") as f:
        f.write(text)
        
def delete_testfile():
    os.remove("test_file.txt")
    
def md5_for_file(f, block_size=2**9):
    md5 = hashlib.md5()
    while True: ## chunk_size = 2**9, prevent reaching memory limit
        data = f.read(block_size)
        if not data:
            break
        md5.update(data) # md5 update with it self so the memory_size of md5 remains the same.
        print(sys.getsizeof(md5) ) # as you can see, md5 is a 32 length string, each str take 2 bytes.
    return md5.hexdigest()

def unit_test():
    text = \
    """
    ENTER WHATEVER YOU WANT TO:
    """ * 32
    create_testfile(text)
    st = time.clock()
    with open("test_file.txt", "rb") as f:
        print(md5_for_file(f) )
    print("elapse time = %s seconds." % (time.clock() - st) )
    delete_testfile()
    
if __name__ == "__main__":
    unit_test()