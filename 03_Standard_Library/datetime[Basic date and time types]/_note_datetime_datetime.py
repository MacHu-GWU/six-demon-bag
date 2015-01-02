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
parse and format a time string
"""

from __future__ import print_function
from datetime import datetime, date, timedelta, tzinfo
import time

def example1():
    """create basic datetime or date object"""
    print("{:=^40}".format("example1"))
    
    print(datetime(2014,9,7,12,15,30))# 2014-09-07 12:15:30
    print(date(2014,9,7))

example1()

def example2():
    """advance datetime I/O method:
        strfttime and strptime
    for more Directive notation, check this link:
        https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
    """
    print("{:=^40}".format("example2"))
    
    print((datetime.strftime( datetime.now(), "[date = %Y-%m-%d][time = %H-%M-%S]"))) # datetime to string
    print((datetime.strptime( "3PM:50:15", "%I%p:%M:%S"))) # string to datetime
    
example2()

def example3():
    """how to use timedelta
    timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)
        https://docs.python.org/2/library/datetime.html#timedelta-objects
    """
    print("{:=^40}".format("example3"))
    
    dt1 = datetime(2014,9,10,18,0,0)
    dt2 = datetime(2014,9,11,20,20,40)
    print((dt2 - dt1, type(dt2 - dt1))) # datetime1 - datetime2 = timedelta
    print((dt1 + timedelta(hours = 24, minutes = 10))) # datetime1 + timedelta = datetime2
    print((timedelta(3) - timedelta(1))) # td2 - td1 = td, default assigned value is day.
    for i in range(10):
        print((dt1 + i*timedelta(1)))
    
example3()

def example4():
    """handle time stamp
    """
    now_local = datetime.now() # get current local time ETZ (UTC-05:00)
    now_utc = now_local + timedelta(hours=5) # get utc time

    now_local_timestamp = now_local.timestamp() # convert datetime to timestamp
    now_utc_timestamp = now_utc.timestamp()

    print(now_local)
    print(now_utc)
    
    print(now_local_timestamp)
    print(now_utc_timestamp)
    
    print(datetime.fromtimestamp(now_local_timestamp)) # convert timestamp to datetime
    print(datetime.fromtimestamp(now_utc_timestamp))
    
example4()