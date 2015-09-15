##encoding=utf-8

"""
BTrees是一个有序二叉树结构, 往数内添加key: value时保持key有序。
doc: https://pythonhosted.org/BTrees/
introduction: http://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
"""

from BTrees.OOBTree import OOBTree
import unittest
import random
import time
import bisect

class OOBTreeCreatePerformance(unittest.TestCase):
    def setUp(self):
        self.complexity = 2**16
        
    def test_create_tree(self):
        array = list(range(self.complexity))
        random.shuffle(array)
         
        st = time.clock()
        d = {i: -i for i in array}
        elapse1 = time.clock() - st
         
        t = OOBTree()
        st = time.clock()
        t.update(d)
        elapse2 = time.clock() - st
         
        print("creating a dict using %.6f sec, a tree %.6f sec" % (elapse1, elapse2))
        self.assertLess(elapse1, elapse2)

class OOBTreeGetItemPerformance(unittest.TestCase):
    def setUp(self):
        self.complexity = 2**16
        self.upper = 4
        self.lower = 2
         
    def test_getitem(self):
        array = list(range(self.complexity))
        random.shuffle(array)
        d = {i: -i for i in array}
        t = OOBTree()
        t.update(d)
        
        st = time.clock()
        for k in array:
            d[k]
        elapse1 = time.clock() - st
         
        st = time.clock()
        for k in array:
            t[k]
        elapse2 = time.clock() - st
        print("get item from a dict using %.6f sec, a tree %.6f sec" % (elapse1, elapse2))
        self.assertLess(elapse1, elapse2)
        
class OOBTreeRangeSearchPerformance(unittest.TestCase):
    def setUp(self):
        self.complexity = 2**16
        self.upper = 4
        self.lower = 2
         
    def test_range_seach(self):
        """
        """
        array = list(range(self.complexity))
        random.shuffle(array)
        d = {i: -i for i in array}
        t = OOBTree()
        t.update(d)
          
        # === dict ===
        st = time.clock()
        result1 = list()
        for k, v in d.items():
            if (self.lower <= k <= self.upper):
                result1.append(v)
        elapse1 = time.clock() - st
  
        # === bisearch ===
        sorted_keys = list(d.keys()) # sort the list of keys
        sorted_keys.sort()
        st = time.clock()
        lower_ind = bisect.bisect_left(sorted_keys, self.lower) # find the min index
        upper_ind = bisect.bisect_right(sorted_keys, self.upper) - 1 # find the max index
        result2 = list() # fetch item
        for ind in range(lower_ind, upper_ind+1):
            result2.append(d[sorted_keys[ind]])
        elapse2 = time.clock() - st
          
        # === tree ===
        st = time.clock()
        result3 = t.values(min=self.lower, max=self.upper, excludemin=False, excludemax=False)
        elapse3 = time.clock() - st
          
        print("results are:", result1, result2, list(result3))
        print("dict method = %.6f, bisearch = %.6f, tree = %.6f" % (elapse1, elapse2, elapse3))
        self.assertGreater(elapse1, elapse2)
        self.assertGreater(elapse2, elapse3)

unittest.main()
    
    
