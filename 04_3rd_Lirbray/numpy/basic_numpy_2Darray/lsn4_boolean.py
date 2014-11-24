##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-01             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""

"""

from __future__ import print_function
import numpy as np

def example1():
    data = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(data >= 5)
    data[data >= 5] = 0
    print(data)
    
# example1()

def example2():
    data = np.array([[1,2,np.NAN], [4,np.NAN,6], [7,8,9]])
    print(np.where( np.isnan(data[0]) ) )
    print(np.where( np.isnan(data) ) )
    
# example2()

def example3():
    data = np.array([[1,2,np.NAN], [4,np.NAN,6], [7,8,9]])
    print(data)
    print(np.where( np.isnan(data).sum(axis=1)==0 ) )
    print(np.where( ~np.isnan(data[:,1])))
example3()