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
pandas.Series是一种带index的一维向量数据容器
reference: http://pandas.pydata.org/pandas-docs/stable/10min.html
"""

from __future__ import print_function
import pandas as pd
import numpy as np
from datetime import date

def create_basic_Series():
    """创建基本序列
    """
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print("=== 原始数据等于 ===\n%s\n" % s)
    
    s = pd.Series([100, 30.5, 21.7, 45, 82, 77, 0.54], index = list("abcdefg"))
    print("=== 原始数据等于 ===\n%s\n" % s)
    
    dates = pd.date_range(start='20130101', periods=7)
    s = pd.Series(np.random.randn(7), index=dates)
    print("=== 原始数据等于 ===\n%s\n" % s)
    print("=== 原始数据前三项等于 ===\n%s\n" % s.head(3) ) # 取得前三项
    print("=== 原始数据后三项等于 ===\n%s\n" % s.tail(3) ) # 取得后三项
    
# create_basic_Series()

def create_time_Series():
    """pandas.date_range(start, end, periods, freq, tz, normalize, name, closed)
    是个功能强大的函数，可以用来生成时间序列。下面是data_range输入参数的文档
        Return a fixed frequency datetime index, with day (calendar) as the default
        frequency
    
        Parameters
        ----------
        start : string or datetime-like, default None
            Left bound for generating dates
        end : string or datetime-like, default None
            Right bound for generating dates
        periods : integer or None, default None
            If None, must specify start and end
        freq : string or DateOffset, default 'D' (calendar daily)
            Frequency strings can have multiples, e.g. '5H'
            
            M = month 可以用12M表示一年
            D = day
            H = hour
            min = minute
            s = second
            
        tz : string or None
            Time zone name for returning localized DatetimeIndex, for example
        Asia/Hong_Kong
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range
        name : str, default None
            Name of the resulting index
        closed : string or None, default None
            Make the interval closed with respect to the given frequency to
            the 'left', 'right', or both sides (None)
    
        Notes
        -----
        2 of start, end, or periods must be specified
    
        Returns
        -------
        rng : DatetimeIndex
    """
    
    dates = pd.date_range(start = "2013-01-01 06:00:00", # start, end, period中的任意两个唯一确定一段时间周期
                          periods = 7,
                          freq = "D", # freq = time delta each period. Default is 1 day. See doc for more option
                          normalize = True) # 强制标准化时间戳到当天的凌晨0点
    print("=========================")
    for dt in dates: print(dt);
    
# create_time_Series()

def downsample_time_Series():
    """对时间数据进行下采样，时间精度变低，样本数量变少
    pandas.Series.resample可以做到这一点
        Convenience method for frequency conversion and resampling of regular
        time-series data.

        Parameters
        ----------
        rule : string
            the offset string or object representing target conversion
        how : string
            method for down- or re-sampling, default to 'mean' for
            downsampling
        axis : int, optional, default 0
        fill_method : string, default None
            fill_method for upsampling
        closed : {'right', 'left'}
            Which side of bin interval is closed
        label : {'right', 'left'}
            Which bin edge label to label bucket with
        convention : {'start', 'end', 's', 'e'}
        kind : "period"/"timestamp"
        loffset : timedelta
            Adjust the resampled time labels
        limit : int, default None
            Maximum size gap to when reindexing with fill_method
        base : int, default 0
            For frequencies that evenly subdivide 1 day, the "origin" of the
            aggregated intervals. For example, for '5min' frequency, base could
            range from 0 through 4. Defaults to 0
    """
    dates = pd.date_range(start="2013-01-01", end="2013-01-07", freq="1min")
    s = pd.Series(np.random.randn(len(dates) ), index=dates)
    print("=== 原始数据等于 ===\n%s\n" % s)
    print("=== 以一天为频率下采样的结果为 ===\n%s\n" % s.resample('D', how='mean'))

# downsample_time_Series()

def upsample_time_Series():
    """对时间数据进行下采样，时间精度变高，样本数量变多，需要进行插值
    pandas.Series.asfreq可以做到这一点
        Convert all TimeSeries inside to specified frequency using DateOffset
        objects. Optionally provide fill method to pad/backfill missing values.

        Parameters
        ----------
        freq : DateOffset object, or string
        method : {'backfill', 'bfill', 'pad', 'ffill', None}
            Method to use for filling holes in reindexed Series
            pad / ffill: propagate last valid observation forward to next valid
            backfill / bfill: use NEXT valid observation to fill method
        how : {'start', 'end'}, default end
            For PeriodIndex only, see PeriodIndex.asfreq
        normalize : bool, default False
            Whether to reset output index to midnight

        Returns
        -------
        converted : type of caller
    """
    dates = pd.date_range(start="2013-01-01", end="2013-01-03 23:59:59", freq="1H")
    s = pd.Series(np.random.randn(len(dates) ), index=dates)
    print("=== 原始数据等于 ===\n%s\n" % s)
    print("=== 以一天为频率上采样的结果为 ===\n%s\n" % s.asfreq('45min', method='pad'))

# upsample_time_Series()