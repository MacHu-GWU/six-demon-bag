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
This document describe how to:
1. capture not only exception and also exception class and message
2. customize your exception message
3. customize your own exception class and behavior
"""

from __future__ import print_function
import sys

def example1():
    """first method to capture exception and print exception information
    sys.exc_info capture the most recent executing information
    """
    def prt_LastError():
        """print last captured exception information"""
        print(sys.exc_info()[0]) # exception class name
        print(sys.exc_info()[1]) # exception index name
        print(sys.exc_info()[2]) # exception memory address
    
    try:
        ans = 1/0
    except:
        prt_LastError()

example1()

def example2():
    """second method to capture exception and print exception information
    Notice:
        except Exception as e: is the python2,3 compatible syntax
    """    
    try:
        ans = 1/0
    except Exception as e: # e is a built-in exception variable, equivalent to sys.exc_info()[1]
        print(e)

example2()

def example3():
    """raise an error and stop executing when Exception.
    simple way to customize the print-out error message.
    """
    try:
        ans = 1/0
    except:
        raise Exception("0 CANNOT be the denominator")
    
# example3()

def example4():
    """Customize your exception
    """
    class FIFO(object):
        def __init__(self, max_length = 1):
            self.array = list()
            self.max_length = max_length
            
        def add(self, item):
            if len(self.array) == self.max_length:
                raise FIFO_exception("full FIFO")
            self.array.append(item)
            
        def pop(self):
            try:
                return self.array.pop()
            except:
                raise FIFO_exception("empty FIFO")
            
    class FIFO_exception(Exception):
        """
        [EN]
        sys.exc_info()[0] = exception class name = "FIFO_exception"
        sys.exc_info()[1] = exception index name = FIFO_exception.__str__   
        [CN]
        exception name 由类名决定
        exception index 由__str__函数决定
        """
        def __init__(self, index):
            """index is for access the proper error message
            """
            self.index = index
            
        def __str__(self):
            """__str__ define the behavior of sys.exc_info()[1], and except Exception, e:
            """
            error_message = {"full FIFO": "cannot add more item into a full FIFO",
                             "empty FIFO": "cannot pop out item from a empty FIFO"}
            return error_message.get(self.index, "Something wrong")
            
    ff = FIFO()
    print("\n=== test FIFO.add exception ===")
    ff.add(1)
    try:
        ff.add(2)
    except:
        print(sys.exc_info()[0]) # exception class name
        print(sys.exc_info()[1]) # exception index name
        print(sys.exc_info()[2]) # exception memory address
    
    print("\n=== test FIFO.pop exception ===")
    ff.pop()
    try:
        ff.pop()
    except:
        print(sys.exc_info()[0]) # exception class name
        print(sys.exc_info()[1]) # exception index name
        print(sys.exc_info()[2]) # exception memory address
    
example4()
