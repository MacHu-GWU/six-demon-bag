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
from geopy.distance import vincenty
from geopy.distance import great_circle

def example1():
    """Calculate distance
    """
    cd1 = (38.953165, -77.396170) # EFA
    cd2 = (38.899697, -77.048557) # GWU
    print("vincenty distance = %s" % vincenty(cd1, cd2).miles)
    print("great_circle distance = %s" % great_circle(cd1, cd2).miles)
    
# example1()

def example2():
    for la in range(28, 48):
        print(vincenty((la, -102.1234), (la, -103.1234)).miles, 
              great_circle((la, -102.1234), (la, -103.1234)).miles)

    for lg in range(-125, -67):
        print(vincenty((34.1234, lg), (35.1234, lg)).miles, 
              great_circle((34.1234, lg), (35.1234, lg)).miles)
        
    
example2()