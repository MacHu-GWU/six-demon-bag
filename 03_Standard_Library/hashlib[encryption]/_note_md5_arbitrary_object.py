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
用pickle.dumps把任意python对象转化成字节流，然后就可以md5了
"""

from __future__ import print_function
import hashlib
import pickle

def md5_obj(obj):
    """return md5 value from a PYTHON OBJECT
    """
    m = hashlib.md5()
    m.update(pickle.dumps(obj) )
    return m.hexdigest()

def unit_test():
    obj = {1: "a"}
    print(md5_obj(obj) )
    
if __name__ == "__main__":
    unit_test()