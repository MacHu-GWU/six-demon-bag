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

"""Description of this scripts
"""

from __future__ import print_function

def example1():
    def add_three_items(a, b, c):
        return a+b+c
    
    three_items = (1,2,3)
    print(add_three_items( *three_items )) # * is to unpack
        
example1()

