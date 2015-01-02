##encoding=utf8

"""
本脚本用于展示与日期有关的时间序列画图。暂时只考虑日期, 不考虑时间。
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime, date, timedelta

def generate_data():
    """x是一年的365天, y是排序后的标准正太分布数据
    """
    n = 365
    start_datetime, td = datetime(2014,1,1,0,0,0), timedelta(1)
    time_list = [start_datetime + td * i for i in range(n)] ## 生成时间轴数据
    
    value_list = np.random.randn(n)
    value_list.sort()
    
    return time_list, value_list

x, y = generate_data()      # 生成数据

def example1():
    """最基本的画图，不对tick, grid, range做任何的调整
    """
    global x, y
    fig = plt.figure()          # 建立画布
    ax = fig.add_subplot(111)   # 建立图
    ax.plot(x, y)               # 画图
    fig.autofmt_xdate()         # 自动调整日期
    plt.show()                  # 显示图片
    
# example1()

def example2():
    """例子: 时间轴按季度标记
    Ticker简介
        在matplotlib中坐标轴上的标记叫做ticker。对于x轴是时间对象的情况，matplotlib.dates中有一系列
        的locator可以帮我们定义要在哪些位置增加ticker。说提供的locator有:
        
            MinuteLocator
            HourLocator
            DayLocator
            WeekdayLocator
            MonthLocator
            YearLocator
            RRuleLocator
            AutoDateLocator
            
            参考网址 ref = http://matplotlib.org/api/dates_api.html#date-tickers
    """
    global x, y
    
    fig = plt.figure()          # 建立画布
    ax = fig.add_subplot(111)   # 建立图
    
    months = dates.MonthLocator([1,4,7,10])     # 设置在哪些位置增加major ticker
    monthFmt = dates.DateFormatter("%Y-%m")     # 设置ticker label格式
    ax.xaxis.set_major_locator(months)          # set major locator
    ax.xaxis.set_major_formatter(monthFmt)      # set major formatter

    fig.autofmt_xdate() # automatically format x axis, 可由于我们自定义了设置, 所以这行可要可不要
    
    ax.plot(x, y)
    plt.xticks(rotation="vertical")
    plt.grid(which="major", axis="x") # 设置grid, 详细参数设置请参考
                                      # http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.grid
    plt.show()
    
# example2()

def example3():
    """例子: 时间轴按月份和周双重标记, 分别自定义grid格式
    ticker对象在matplotlib中被分为major和minor两类。大ticker和小ticker互相独立不影响。
    所以我们可以分别对两种ticker的区间，label文字，线型进行定义
    """
    global x, y
    
    x, y = x[:90], y[:90] # 在本例中我们只使用1-3月的数据
    
    fig = plt.figure()          # 建立画布
    ax = fig.add_subplot(111)   # 建立图
     
    months = dates.MonthLocator([1,2,3])     # 设置在哪些位置增加major ticker
    monthFmt = dates.DateFormatter("%Y-%m")     # 设置ticker label格式
    ax.xaxis.set_major_locator(months)          # set major locator
    ax.xaxis.set_major_formatter(monthFmt)      # set major formatter

    weekdays = dates.WeekdayLocator(byweekday=6)
    weekdayFmt = dates.DateFormatter("%m-%d %a")
    ax.xaxis.set_minor_locator(weekdays)        # set minor locator
    ax.xaxis.set_minor_formatter(weekdayFmt)    # set minor formatter
    
    fig.autofmt_xdate() # automatically format x axis, 可由于我们自定义了设置, 所以这行可要可不要
    
    ax.plot(x, y)
    plt.xticks(rotation="vertical")
    
    plt.grid(which="major", axis="x", color="r", linestyle="-", linewidth=2)    # 设置major grid
    plt.grid(which="minor", axis="x", color="k", linestyle="--", linewidth=1)   # 设置minor grid
    
    # plt.setp是一个很强大的函数。可以对所有的对象单独进行设置。plt.setp(object, **kwarg)
    plt.setp( ax.xaxis.get_majorticklabels(), rotation=70 ) # 设置major tick label
    plt.setp( ax.xaxis.get_minorticklabels(), rotation=90 ) # 设置minor tick label
    
    plt.show()
    
# example3()