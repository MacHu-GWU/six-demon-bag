##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-18             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
how to get currently running python version information
"""

from __future__ import print_function # python2,3 compatible print function
import sys # system 
import six # Python 2 and 3 Compatibility Library

print(sys.version_info[0], type(sys.version_info[0]))
print(sys.version[0], type(sys.version[0]))
print(six.PY2)
print(six.PY3)