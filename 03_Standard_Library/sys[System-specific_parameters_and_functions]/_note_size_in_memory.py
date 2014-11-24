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

from __future__ import print_function
import sys

INT1 = 65535
INT2 = 12345678901234567890
FLOAT1 = 3.1415926535
FLOAT2 = 1234567890.123456789012345678901234567890
STR = "abcd"
LIST = ["a", "b", "c", "d"]
SET = {"a", "b", "c", "d"}
DICT = {"a":1, "b":2, "c":3, "d":4}

for i in [INT1, INT2, FLOAT1, FLOAT2, STR, LIST, SET, DICT]:
    print("%s = %s" % (i, sys.getsizeof(i)))