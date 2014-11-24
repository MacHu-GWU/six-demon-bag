##coding=utf8

import pprint

answer = \
{"step1" : {1: "a",
            2: "b",
            3: "c"},
 "step2" : {1: "e",
            2: "f",
            3: "g"},
 "step3" : {1: "h",
            2: "i",
            3: "j"}
}

data = dict()
 
with open("data.txt", "rb") as f:
    start_flag = 0
    counter = 0
    for line in f.xreadlines():
        
        if "step" in line: # 遇到开始的信号
            start_flag = 1 # 打开数据录入开关
            counter += 1 # 1级 key 编号自增1
            key1 = "step%s" % str(counter).zfill(1) # 保存 1级 key
            data[key1] = dict() ## 初始化数据容器
            line_counter = 0 ## 初始化行计数器
            continue
        
        elif start_flag: # "step"不在里面，然后检测flag是否已经打开了
            line_counter += 1
            data[key1].setdefault(line_counter, line.strip())
            
pprint.pprint( data )
pprint.pprint( answer )