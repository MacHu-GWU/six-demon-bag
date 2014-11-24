##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

import memory_profiler  
import random
# import sys

# @profile
def qsort(L):
    if len(L) <= 1: 
        return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + qsort([ge for ge in L[1:] if ge >= L[0]]) 


if __name__ == '__main__':
    L = range(1,10000)
    random.shuffle(L)
#     print L, '\n'
    qsort(L)

# ###################### 快速排序的流程演示 ###########################
# 原始数据是： [5, 4, 2, 9, 1, 3, 6, 8, 7, 10]
# 为了表达方便，我们对快速排序中的三个关键部分分别定义为： "small" "key" "large"
# 所以整个排序过程可以表示如下：
# [5, 4, 2, 9, 1, 3, 6, 8, 7, 10] (最后是[1,2,3,4,5,6,7,8,9,10])
# |--- key = 5
# |--- small = [4,2,1,3] (最后是[1,2,3,4])
#     |--- key = 4
#     |--- small = [2,1,3] (最后是[1,2,3])
#         |--- key = 2
#         |--- small = 1
#         |--- large = 3
#         |--- 合并成 [1,2,3]
#     |--- large = [] (最后是[])
#     |--- 合并成 [1,2,3,4]
# |--- large = [9,6,8,7,10] (最后是[6,7,8,9,10])
#     |--- key = 9
#     |--- small = [6,8,7] (最后是[6,7,8])
#         |--- key = 6
#         |--- small = []
#         |--- large = [8,7] (最后是[7,8])
#             |--- key = 8
#             |--- small = 7
#             |--- large = []
#             |--- 合并成 [7,8]
#         |--- 合并成 [6,7,8]
#     |--- large = 10
#     |--- 合并成[6,7,8,9,10]