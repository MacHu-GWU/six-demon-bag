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

from __future__ import print_function
import pandas as pd
import numpy as np

def example1():
    df = pd.DataFrame({"a" : ["one", "one", "two", "three", "two", "one", "six"],
                       "b" : ["x", "y", "y", "x", "y", "x", "x"],
                       "c" : np.random.randn(7)})
    for ID, row in df.iterrows(): # ID = row index, row = row series (with row index)
        print("=== number of row %s ===\n%s\n" % (ID, row) )
     
    for ID, column in df.iteritems(): # ID = column index, rolumn = column series (with column index)
        print("=== column of %s ===\n%s\n" % (ID, row) )
        
    for i in df.itertuples(index=False): # iter rows as tuple, if index=True, then index is the first element in returned tuple
        print(i)
        
example1()