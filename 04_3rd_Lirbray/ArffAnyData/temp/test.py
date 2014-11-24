##coding=utf8
##By. Sanhe 2014-06-09
##[标题] 如何从txt或csv文件中读取数据

import numpy as np
from StringIO import StringIO

fname3 = 'dump_data3.txt' ## 如果要从csv文件中读取，只需要改变扩展名为csv即可

''' 本例中，每列中 的数据被定义成了不同的数据类型 '''
with open(fname3, 'rb') as text:
    data = np.genfromtxt(   StringIO(text.read()), 
                            delimiter=",", ## 定义分隔符
                            dtype = [('x', int), ('y', float), ('z', 'S10')], ## 定义数据类型
                            skiprows = 0, ## 从头跳过若干行
                            skip_header = 0, ## 跳过第一行标题
                            skip_footer = 0) ## 跳过最后一行注脚

