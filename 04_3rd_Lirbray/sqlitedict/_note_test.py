##encoding=UTF8

"""
sqlitedict是一个用sqlite数据库来保存大字典的库。因为对超大字典进行IO的时候我们往往难以承受读写的
时间。 虽然sqlitedict在对值进行访问, 修改的速度上不如内存字典, 但是在IO的时候时间大大节省了。
"""

from __future__ import print_function, unicode_literals
from sqlitedict import SqliteDict
from datetime import datetime, date, timedelta

def basic_usage():
    """SqliteDict引擎会将任意的value转换为
    """
    mydict = SqliteDict("test.sqlite", autocommit=True)
    mydict["integer_value"] = 1
    mydict["real_value"] = 2.2
    mydict["text_value"] = "abc"
    mydict["date_value"] = date.today()
    mydict["datetime_value"] = datetime.now()
    
    # if you don't use with SqliteDict("test.sqlite") as mydict: ...
    # you have to close the connection explicitly
    mydict.close() 
    
basic_usage()

def test_mutiple_thread():
    """多个进程访问数据库的时候, 最好只有一个有写操作。如果需要多个进程进行写操作, 则需要每次在
    写操作后进行commit, 也就是说需要打开autocommit
    """
    dict1 = SqliteDict("test.sqlite", autocommit=False) # if False, then mutiple thread writing is
    dict2 = SqliteDict("test.sqlite", autocommit=False) # not allowed
    print(dict1["integer_value"])
    print(dict2["integer_value"])

#     dict1["integer_value"] = 2
    print(dict1["integer_value"], dict2["integer_value"])
    
#     dict2["integer_value"] = 3
    print(dict1["integer_value"], dict2["integer_value"])
    
    dict1.close()
    dict2.close()
    
test_mutiple_thread()
