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
ref = https://docs.python.org/2.7/library/pickle.html
ref = https://docs.python.org/3.4/library/pickle.html

说明：
    python2和python3的pickle所产生的文件不能互通（虽然理论上
    是可以通过设定protocol来兼容，但是由于写操作的作用机理不同，
    所以很容易导致不可预见的错误）
    
用法：
    pickle.dump(object, open("fname.p", "w"))
"""

from __future__ import print_function
import pickle
import base64
import sys

def example1():
    """write to file
    pickle.dump(obj, file) serialize obj and write it to file

    pickle.dumps(obj) returns the following instead of writing to file
        str in python2
        bytes in python3
    """
    obj = [1,2,3,4]
    print( type(pickle.dumps(obj)), "in python%s" % sys.version_info[0] )
    
    pickle.dump(obj, open("obj.p", "wb"), protocol = 2) # 指定 protocol = 2，这样在python3中dump的pickle在python2也能读
    print( pickle.load(open("obj.p", "rb")) )

# example1()

def example2():
    """pickle any python object and make it string like. Then it's very easy to deliver and
    save to database.
    For more information, see base64 in python
    """
    obj = {1:"a", 2:"你好"}
    pk = pickle.dumps(obj, protocol = 2) # make it 2, 3 compatible
    encoded = base64.b64encode(pk) # encode arbitrary binary strings into text strings
    print(type(encoded), encoded)  # it's a text string in bytes
    print(type(str(encoded)), str(encoded))
    print(pickle.loads(base64.b64decode(encoded) ) ) # see if we can recovery the obj from text string
    
example2()