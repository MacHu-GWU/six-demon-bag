## coding=utf8
# ========== Define Backpack problem ===========
#    GUID    Space    Value    Available Number
#    1        5        6            7
#    2        3        4            10
#    3        2        7            3
# 1. unlimited number (negelect the available number)
#    Given X unit space, select item to maximize the Value
# 2. limited number
#    Given X unit space, select item to maximize the Value

import pickle

data_fname = 'subjects.txt'

with open(data_fname, 'r') as f:
    ## data keys = [1,2,3, ...]
    ## data value = {'space': , 'value': , 'ratio': }
    data = dict()
    i = 1
    for line in f:
        [a,b,c] = line.strip().split(',')
        data[i] = {'space':int(b),'value':int(c),'ratio':float(c)/float(b)}
        i += 1

pickle.dump(data, open('data_BackpackProblem.p', 'w'))
    