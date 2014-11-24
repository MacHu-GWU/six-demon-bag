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

"""
Repack of datetime standard library
    1. generate day, month, year interval start, end timestamp for SQL datetime related query.
    
compatibility: python2, python3

prerequisites: None

import:
    from HSH.Data.timewrapper import TimeWrapper
"""

from __future__ import print_function
from datetime import datetime as dt, date as dd, timedelta as td
import itertools

class TimeWrapper(object):
    def __init__(self):
        ## 创建所有的模板
        year_formats = ["%Y", "%y"]
        month_formats = ["%m", "%b", "%B"]
        day_formats = ["%d"]
        pads = ["/", "-", " "]
        templates, counter = dict(), 0        
        for orders in itertools.permutations([year_formats, month_formats, day_formats], 3):
            for od in [(od0, od1, od2) for od0 in orders[0] for od1 in orders[1] for od2 in orders[2] ]:
                for pad in pads:
                    templates[counter] = pad.join(od)
                    counter += 1
                    
        self.templates = templates
        self.default_template = None
        self.iso_dateformat = "%Y-%m-%d"

    def reformat(self, dtstring, before, after):
        """将dtstring从原来的#before格式转换成#after格式"""
        DT = dt.strptime(dtstring, before)
        return dt.strftime(DT, after)
    
    def iso_date(self, datestr):
        """Try strip date string from our 108 templates and convert to ISO date format
         If None template matching datestr matching, then raise Error
         
         第一次调用时，默认模板是空的。所以对所有模板进行尝试，如果成功，则把模板保存下来。以后尝试
         先尝试这个默认模板，如果失败了，再重新对所有模板进行尝试
        """
        if self.default_template: # 如果已经有了默认的模板设置
            try:
                return dt.strftime(dt.strptime(datestr, 
                                               templates[self.default_template]), 
                                   "%Y-%m-%d")
            except: # 如果默认的模板不匹配，则重新尝试所有的模板
                for ind, template in self.templates.items(): # 对每个template进行尝试，如果都不成功，抛出异常
                    try:
                        iso_date = self.reformat(datestr, template, self.iso_dateformat) # 如果成功了
                        self.default_template = ind # 保存index到iso_dateformat
                        return iso_date
                    except:
                        pass
                raise Exception("None template matching datestr")
        else: # 如果还没有，尝试所有的模板
            for ind, template in self.templates.items(): # 对每个template进行尝试，如果都不成功，抛出异常
                try:
                    iso_date = self.reformat(datestr, template, self.iso_dateformat) # 如果成功了
                    self.default_template = ind # 保存index到iso_dateformat
                    return iso_date
                except:
                    pass
            raise Exception("None template matching datestr")