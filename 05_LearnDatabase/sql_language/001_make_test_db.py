##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-31             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""Make the test db for demonstration
"""

from __future__ import print_function
from sqlalchemy import create_engine
import pandas as pd
import sqlite3
Excel2db.xlsx_to_sqlite("wc3_demo_db.xlsx")