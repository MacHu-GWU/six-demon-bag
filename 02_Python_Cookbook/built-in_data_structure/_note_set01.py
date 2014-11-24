##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function

"""
set.intersection(set1, set2, set3, ...) 的确是一个很强大的函数
但是它不支持set.interestion( [set1, set2, set3, ...] ) 这样的语法
或者对于一系列generator所生成的set, set.intersection默认的语法就
不太方便了。所以我们编写了:
    intersect_all
    union_all
    两个函数以解决这一问题
"""

def intersect_all(list_of_set):
    """
    list_of_set can be a list or a generator object
    """
    res, flag = set(), 1
    for jihe in list_of_set:
        if flag:
            res.update(jihe)
            flag = 0
        else:
            res.intersection_update(jihe)
    return res

def union_all(list_of_set):
    """
    list_of_set can be a list or a generator object
    """
    res = set()
    for jihe in list_of_set:
        res.update(jihe)
    return res

if __name__ == "__main__":
    def gen(list_of_set):
        for i in list_of_set:
            yield i
    
    print(intersect_all(gen([{1,2,3}, 
                             {2,3,4}, 
                             {3,5,6}])))
    print(intersect_all([{1,2,3}, 
                         {2,3,4}, 
                         {3,5,6}]))
    print(union_all(gen([{1,2,3}, 
                         {2,3,4}, 
                         {3,5,6}])))
    print(union_all([{1,2,3}, 
                     {2,3,4}, 
                     {3,5,6}]))

