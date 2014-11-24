##coding=utf8
import os
from StringIO import StringIO
import arff
import numpy as np
import pandas as pd

class DataTransformer(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return str(self.data)
    
    def _load_txt(self, path, dtypedefine, skip_header):
        ''' 从txt文件中产生 pandas 数据容器
        '''
        with open(path, 'rb') as text:
            if dtypedefine == None: ## default data type define is str
                dtypedefine = 'str'
                data = np.genfromtxt(   StringIO(text.read()), 
                                        delimiter=",", ## 定义分隔符
                                        dtype = dtypedefine, ## 定义数据类型
                                        skip_header = skip_header) ## 跳过表头
                data = pd.DataFrame(data, ## columns 自动从A-Z编号，列数不得超过12列
                                    columns = [ str(chr(i)) for i in range(65,91) ][:data.shape[1]] )
            else:
                data = np.genfromtxt(   StringIO(text.read()), 
                                        delimiter=",", ## 定义分隔符
                                        dtype = dtypedefine, ## 定义数据类型
                                        skip_header = skip_header) ## 跳过表头
                data = pd.DataFrame(data, ## 根据dtypedefine中的定义，定义列名称
                                    columns = zip(*dtypedefine)[0] )
        return data

    def _load_csv(self, path, dtypedefine, skip_header):
        ''' 从txt文件中产生 pandas 数据容器
        '''
        with open(path, 'rb') as text:
            if dtypedefine == None: ## default data type define is str
                dtypedefine = 'str'
                data = np.genfromtxt(   StringIO(text.read()), 
                                        delimiter=",", ## 定义分隔符
                                        dtype = dtypedefine, ## 定义数据类型
                                        skip_header = skip_header) ## 跳过表头
                data = pd.DataFrame(data, ## columns 自动从A-Z编号，列数不得超过12列
                                    columns = [ str(chr(i)) for i in range(65,91) ][:data.shape[1]] )
            else:
                data = np.genfromtxt(   StringIO(text.read()), 
                                        delimiter=",", ## 定义分隔符
                                        dtype = dtypedefine, ## 定义数据类型
                                        skip_header = skip_header) ## 跳过表头
                data = pd.DataFrame(data, ## 根据dtypedefine中的定义，定义列名称
                                    columns = zip(*dtypedefine)[0] )
        return data
    
    def load(self, path, define = None, skip_header = 0):
        ''' [主要功能]更新self.data内的数据，能做到自动根据文件类型调节
        '''
        support_type = ['.txt', '.csv', '.arff']
        ext = os.path.splitext(path)[1]
        if ext not in support_type:
            print 'this type of data file are not supported'
        else:
            self.data = eval('self._load_%s(path, define, skip_header)' % ext[1:])
            

fname = 'dump_data3.csv'
dt = DataTransformer('sanhe')
# dt.load(fname)
dt.load(fname, [('one', int),('two', float),('three', 'S10')])
print dt