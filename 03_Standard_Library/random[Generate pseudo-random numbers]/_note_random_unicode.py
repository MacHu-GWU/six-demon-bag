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
import random
import time

def rand_string1(length):
    '''Generate arbitrary long random string
    Performance: 
        generate 50k 32-length random string per second
        for 32-length string, there are 2.27e57 different choices
    '''
    test_chars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    s = []
    for i in xrange(length): # naive method
        s.append(random.choice(test_chars))
    return "".join(s)

def rand_string2(length):
    '''Generate arbitrary long random string
    Performance: 
        generate 58k 32-length random string per second, 15% faster
        for 32-length string, there are 2.27e57 different choices
    '''
    test_chars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" * length
    return "".join(random.sample(test_chars, length) ) # built-in random.sample function

def performance_test():
    st = time.clock()
    for i in xrange(50000):
        text = rand_string1(32)
    print(time.clock() - st)
    
    st = time.clock()
    for i in xrange(50000):
        text = rand_string2(32)
    print(time.clock() - st)
        
if __name__ == '__main__':
    performance_test()