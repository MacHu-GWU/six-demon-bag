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
sys.exc_info() returns a tuple of three values that give information about 
the exception that is currently being handled

0. exception type
1. exception itself
2. traceback object
"""

from __future__ import print_function
import sys

try:
    a = [1,2,3]
    b = a + 1
except:
    print(sys.exc_info())
    print("[%s][%s]" % (sys.exc_info()[0], type(sys.exc_info()[0]) ) )
    print("[%s][%s]" % (sys.exc_info()[1], type(sys.exc_info()[1]) ) )
    print("[%s][%s]" % (sys.exc_info()[2], type(sys.exc_info()[2]) ) )