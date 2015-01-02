##encoding=utf8

"""
本脚本用于展示与日期时间有关的画图。
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime, date, timedelta

def generate_data(start_date, end_date, interval_in_second):
    """从起始日期的00:00:00到结束日期的23:59:59, 按照间隔#interval_in_second秒采样, 生成数据.
    """
    td = timedelta(seconds=interval_in_second)
    
    time_list = list()
    for i in range(1000000):
        if start_date + i * td <= end_date:
            time_list.append(start_date + i * td)
        else:
            break
        
    value_list = np.random.randn(len(time_list))
    value_list.sort()
    return time_list, value_list

x, y = generate_data(datetime(2014,1,1,0,0,0), datetime(2014,1,31,23,59,59), 3600)
