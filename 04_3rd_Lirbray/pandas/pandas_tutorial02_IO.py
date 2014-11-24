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
[标题]Data IO Syntax in Pandas
"""

from __future__ import print_function
import numpy as np
import pandas as pd
import datetime


""" === 读操作 === """

def read_csv():
    """从txt, csv中读取数据
    从txt, csv中读取数据时, 可以对每列的数据类型进行预定义。这一点是read_excel无法做到的
    """
    print("{:=^40}".format("read from csv"))
    df = pd.read_csv(r"resources/employee.csv", 
                     sep = ",", # 列分隔符, default = ","
                     usecols = [0,1,2,3,4], # 只读某几列, 等于read_excel中的parse_cols参数
                     header = 0, # 没有表头 = None, 第一行是表头 = 0, 第n行是表头 = n-1; default = 0
                     index_col = False, # 没有行 = False, 第一列是行index = 0, 第n列是行index = n-1; default = False 
                     skiprows = 0, # 跳过前面n行不读
                     dtype = {"id": np.str, # 强制定义数据类型, 如果不定义, id默认就是整数了
                              "name": np.str, 
                              "height": np.float64, 
                              "age": np.int64, 
                              },
                     nrows = 9999) # 只读前n行
                     
    print(df)
    print(type(df.loc[0, "id"])) # 由于已经定义了是str, 所以是str
    print(type(df.loc[0, "enroll_date"])) # 默认时间日期是str


    print("{:=^40}".format("read from txt"))
    df = pd.read_csv(r"resources/employee.txt",
                     sep = "\t", # 列分隔符, default = ","
                     usecols = [0,1,2,3,4], # 只读某几列, 等于read_excel中的parse_cols参数
                     header = 0, # 没有表头 = None, 第一行是表头 = 0, 第n行是表头 = n-1; default = 0
                     index_col = False, # 没有行 = False, 第一列是行index = 0, 第n列是行index = n-1; default = False 
                     skiprows = 0, # 跳过前面n行不读
                     dtype = {"id": np.str, # 强制定义数据类型, 如果不定义, id默认就是整数了
                              "name": np.str, 
                              "height": np.float64, 
                              "age": np.int64, 
                              },
                     nrows = 9999) # 只读前n行
                     
    print(df)
    print(type(df.loc[0, "id"])) # 由于已经定义了是str, 所以是str
    print(type(df.loc[0, "enroll_date"])) # 默认时间日期是str
    
# read_csv()

def read_excel():
    """从excel中读取数据
    read_excel无法在读取前预先对每列的数据类型进行定义。
    """
    print("{:=^40}".format("read from excel"))
    df = pd.read_excel(r"resources/employee.xlsx", # read_excel 也有 header, index_col的设置, 此处略过
                       "employee", # worksheet name
                       parse_cols = [1,2,3,4,5], # 只读某几列, 等于read_csv中的usecols参数
                       header = 0, # 没有表头 = None, 第一行是表头 = 0, 第n行是表头 = n-1; default = 0
                       index_col = 0, # 没有行index = False, 第一列是行index = 0, 第n列是行index = n-1; default = False
                       skiprows = 0, # 跳过前面n行不读
                       ) 
    print(df)
    print(df.index)
    
# read_excel()

def read_json():
    """只支持二维表类别的json. 换言之json数据的格式看起来应该是下面的样子:
    {
        "index1": {
            "column1": value
            "column2": value
            ...
        }
        ...
    }
    """
    print("{:=^40}".format("read from json"))
    df = pd.read_json(r"resources/employee.json", orient="index")
    print(df)
    
# read_json()

def to_csv():
    """把数据写入csv中
    """
    print("{:=^40}".format("write to csv"))
    df = pd.DataFrame([(1, "bob", 1.73, 25, datetime.date(2014,1,1)),
                       (2, "dan", 1.82, 43, datetime.date(2014,3,7)),
                       (3, "jane", 1.64, 31, datetime.date(2014,2,13))], columns = ["ID",
                                                                                      "name",
                                                                                      "height",
                                                                                      "age",
                                                                                      "enroll_date"])
    df.to_csv("employee_info.csv", 
              header = True, # 是否写入columns
              index = False, # 是否写入index
              encoding = "utf8", # 编码
              chunksize = 1, # 一次从内存中写入多少行. 当表特别大的时候, 可以用于节约内存
              tupleize_cols = False) # ref = http://pandas.pydata.org/pandas-docs/dev/io.html#io-store-in-csv

# to_csv()

def to_excel():
    """把数据写入Excel文件中
    注: 在windows平台下, 预编译的scipy-stack的exe安装包里里面已经包含了lxml包, 所以可以直接运行。
    但是在mac或linux平台下
    """
    print("{:=^40}".format("write to excel"))
    cindex1, cindex2 = "ABCD", "abcdefg"
    df1 = pd.DataFrame(np.random.randn(6,4), columns = list(cindex1) )
    df2 = pd.DataFrame(np.random.randn(10,7), columns = list(cindex2) )
    writer = pd.ExcelWriter("output.xlsx")
    df1.to_excel(writer, "Sheet1", index = False, # 是否把index放在第一列写入?
                                   header = False, # 是否把columns放在第一行写入?
                                   )
    df2.to_excel(writer, "Sheet2")
    writer.save()
    
# to_excel()

def to_json():
    """把数据写入json
    """
    print("{:=^40}".format("write to json"))
    df = pd.DataFrame([["john", 18],
                       ["sam", 34]], columns = ["name", "age"])
    df.to_json("person.json", orient="index")
    
to_json()

def example1():
    """各种数据类型被写入Excel文件后的变化
    所支持的：
        int, float, str, datetime, date, boolean, None
    所不支持的：
        list, tuple, set, dict
    
#     data = [(1, 34.28863312, "bob", datetime(2001,1,1,0,0,0), date(1998,1,1), True, None, [1,2,3], (1,2,3), {1,2,3}, {1:"a"}),
#             (2, 2.4423423, "jack", datetime(2001,1,1,0,6,30), date(1998,2,1), False, None, [3,2,1], (3,2,1), {3,2,1}, {2:"b"}),]
#     df = pd.DataFrame(data, columns = ["int", "float", "str", "datetime", "date", "boolean", "None", "list", "tuple", "set", "dict"])

    """
    print("{:=^40}".format("example23"))
    data = [(1, 34.28863312, "bob", datetime(2001,1,1,0,0,0), date(1998,1,1), True, None),
            (2, 2.4423423, "jack", datetime(2001,1,1,0,6,30), date(1998,2,1), False, None)  ]
    df = pd.DataFrame(data, columns = ["int", "float", "str", "datetime", "date", "boolean", "null"])
    writer = pd.ExcelWriter("data_types.xlsx")
    df.to_excel(writer, "Sheet1", index = False, header = True)    
    writer.save()
    
# example1()
