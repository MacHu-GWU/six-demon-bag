##encoding=utf8

"""
data.txt文件中有1000个格式杂乱不一的日期，要求在30秒内能将所有1000个日期处理成标准日期格式：
2014-01-20    4位数字年份-两位数月份-两位数日期
"""

from __future__ import print_function
import time


def main():
    """put your code down here"""
    
    
if __name__ == "__main__":
    st = time.clock()
    main()
    print("elapse time = {0}".format(time.clock() - st) )