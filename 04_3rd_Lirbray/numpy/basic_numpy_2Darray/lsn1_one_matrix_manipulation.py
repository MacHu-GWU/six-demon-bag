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
注意！！ Numpy矩阵是一个以行向量为导向的矩阵
"""

from __future__ import print_function
import numpy as np

def example1():
    """ === 建立矩阵  === """
    print("{:=^40}".format("example1"))
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    print("data1为:\n%s\n" % data)

# example1()

def example2():
    """ === 矩阵转置  ==="""
    print("{:=^40}".format("example2"))
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    print(np.transpose(data))
    print(data.transpose())

# example2()

def example3():
    """ === 取得元素，行，列  === 
    numpy是一个以行为导向的阵列
    """
    print("{:=^40}".format("example3"))
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    print(data[1]) # 取第2行
    print(data[0:2]) # 取1-2行，slice表达式
    print(data[[0,2]]) # index表达式
    
    print(data[:,1]) # 取第2列，由于只有一列，所以自动转化为向量
    print(data[:,0:2]) # 取1-2列，slice表达式
    print(data[:,[0,2]]) # index表达式
    
    print(data[np.ix_([0,1], [0,1])])
    
    print(data[(0,1)]) # 取第1行第2个元素
    
    print(data[(data > 4.5) & (data < 6.5)]) # 取所有满足条件的数
    
# example3()

def example4():
    """ === 建立等差数列  === """
    print("{:=^40}".format("example4"))
    data1 = np.linspace(1,10,6) # (start, end, num) 从1到10，共6个元素
    print(data1)
    data2 = np.arange(1,10,1.5) # (start, end, step) 从1到10，每隔1.5取一个
    print(data2)
    
# example4()

def example5():
    """ === 建立基本 0矩阵 1矩阵 对角矩阵 === """
    print("{:=^40}".format("example5"))
    print(np.zeros((2,3)) )
    print(np.ones((2,3)) )
    print(np.eye(2,3) )
    print(np.ones_like([[1,2,3],[4,5,6]]) )## 生成跟 np.ones_like(array) 大小一样的矩阵

# example5()

def example6():
    """ === 与矩阵大小有关的操作 ===
    1. 取得矩阵大小
    2. 改变矩阵形状
    3. 压平变成行向量
    4. 行列向量变换
    """
    print("{:=^40}".format("example6"))
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9],
                     [10,11,12]])
    print(data.shape)
    print("矩阵变换成4*3的矩阵:\n", data.reshape(4,3))
    print("矩阵resize之前是:\n", data)
    data.resize((2,6)) # 注意！此方法会改变矩阵本身
    print("矩阵resize之后是:\n", data)
    print(data.flatten() ) # 将矩阵压平
    
    data_row = np.array([1,2,3])
    data_column = np.array([[1],[2],[3]])
    print("行变成列:\n", data_row[np.newaxis].transpose()) # 行向量变列向量
    print("列变成行:\n", data_column.transpose()[0]) # 列向量变行向量
    """ 3. 变换数据类型  """
#     print(data1.astype("int") ) 

# example6()

def example7():
    """数据类型变换
    数据类型可以参考 http://docs.scipy.org/doc/numpy/user/basics.types.html
    """
    data = np.array([[ 0.52631555, -0.67881092,  0.01858068],
                     [-0.25417718, -1.46325551,  0.45669787],
                     [-1.13090243, -0.69264103,  0.61054582]])
    print(data.astype(int))
    print(data.astype(str))
    np.set_printoptions(precision=4) # 修改打印精度
    print(data)
    
# example7()

def example8():
    """ === 矩阵内部元素运算 ===
    所有的方法都是针对全部的元素，而不像matlab中的列向量
    """
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    print(data.max() ) # 最大值
    print(data.min() ) # 最小值
    print(data.sum() ) # 求和
    print(data.cumsum() ) # 累积和
    print(data.prod() ) # 积
    print(data.cumprod() ) # 累计积
    print(data.all() ) # 如果所有元素为真，则返回真，否则返回假
    print(data.any() ) # 只要有一个元素为真则返回真
    print(np.diff(data) ) # 差分
    print(np.unique(np.array([[1,1,2,2,3,3],        # 求distinct value
                              [2,2,3,3,4,4]]) ) )

# example8()

def example9():
    """ === 向量对象 ===
    定义SUM符号表示 SUM = (x1-u)^2 + (x2-u)^2 + ...
    """
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    print(data.mean() ) # 求均值 mean
    print(data.var() ) # 方差 (SUM/N)
    print(data.std() ) # 标准差 (SUM/N) ** 0.5
    print(np.average(data.flatten(), weights = [9,8,7,6,5,4,3,2,1]) ) # 加权平均
    print(np.median(data) )# 中位数

# example9()

def example10():
    """ === 矩阵对象 === """
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    print(data.mean(axis = 0, # 0 = 按列求平均, 1 = 按行求平均
                     keepdims = 1), "均值" ) # keepdims = 0 输出1纬向量, = 1输出2纬矩阵
    print(data.var(axis = 0, # 0 = 按列求平均, 1 = 按行求平均
                     keepdims = 1), "方差" )# 输出2纬向量
    print(data.std(axis = 0, # 0 = 按列求平均, 1 = 按行求平均
                     keepdims = 1), "标准差" ) # 输出2纬向量

# example10()