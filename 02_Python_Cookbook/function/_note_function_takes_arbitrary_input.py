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

from __future__ import print_function

def print_everything(*args):
    """
    *args = list of arguments - as positional arguments
    "args" can be replaced by any word
    """
    for count, thing in enumerate(args):
        print("{0}. {1}".format(count, thing))
        
# print_everything("apple", "banana", "cabbage")

def table_things(**kwargs):
    """
    **kwargs = dictionary - whose keys become separate keyword arguments and the values become values of these arguments.
    "kwargs" can be replaced by any word
    """
    for count, thing in kwargs.iteritems():
        print("{0}. {1}".format(count, thing))
        
# table_things(apple = "fruit", cabbage = "vagetable")

a = {"apple": "fruit", "cabbage": "vagetable"}
table_things(**a)