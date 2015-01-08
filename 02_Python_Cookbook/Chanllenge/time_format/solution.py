##encoding=utf8

from __future__ import print_function
from timewrapper import TimeWrapper
import time

def main():
    tw = TimeWrapper()
    res = list()
    with open("data.txt", "r") as f:
        for line in f.readlines():
            res.append(str(tw.str2date(line.strip() ) ) )
    
    with open("result.txt", "w") as f:
        f.write("\n".join(res))
            
if __name__ == "__main__":
    st = time.clock()
    main()
    print("elapse time = {0}".format(time.clock() - st) )
    
"""
思考，还能怎么优化？

给一个思路。比如我们有100万个日期，我们可以对我们的模板一个个试验的同时，记录每个模板已经匹配到的数量。
一旦默模板不能用，按照平常的做法我们是一个个试过来，但是我们由于已经记录了以前所匹配到的数量，我们对于
一个新的样本，我们有理由从以前匹配到数量最多的模板开始往下试验，这样命中率会高一些。
"""
    