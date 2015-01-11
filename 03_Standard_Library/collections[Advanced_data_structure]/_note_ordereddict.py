##encoding=utf8



# Ref=https://docs.python.org/2/library/collections.html?highlight=ordereddict#ordereddict-objects

"""

"""

from __future__ import print_function
import sys
from collections import OrderedDict

def compare_normal_dict_with_ordered_dict():
    """ordered dict iterate items by the order the key originally inserted
    """
    d = dict()
    d["A"] = 3
    d["B"] = 2
    d["C"] = 1
    od = OrderedDict()
    od["A"] = 3
    od["B"] = 2
    od["C"] = 1
    print("{:=^100}".format("key order in regular dict is random"))
    for k in d:
        print(k)
    
    print("{:=^100}".format("key order in ordered dict is the order key been inserted"))
    for k in od:
        print(k)

# compare_normal_dict_with_ordered_dict()

def regulardict_to_ordereddict():
    """sort a dict by it's key, value, or customized rules. user can choose ascend or descend.
    OrderedDict其实并不是生成一个全新的字典。OrderedDict只是生成了一个新的Key的序列, 然后通过维护这个
    Key序列来决定输出的顺序。
    
    如果 d 的 key 和 value 都是可排序的数字或者字符串, 而我们不引用任何复杂的规则, 仅仅是根据key或者
    value来排序, 那么生成的OrderedDict的内存开销就不变, 因为仅仅是在调用iter方法时, 临时排序输出即可。
    而如果使用形如:
        根据value中第二个元素进行排序
    那么就会带来额外的内存开销。本例中就是这种情况。
    """
    d = {"c":[1, 3],
         "a":[3, 2],
         "b":[2, 1]}
    
    print("{:=^100}".format("sort by value, ascend"))
    od1 = OrderedDict( sorted(list(d.items()), 
                             key=lambda t: t[1], # t[0]指根据key排序, t[1]指根据value排序
                             reverse = False) ) # True指逆序排序，False指正序排序
    for k,v in list(od1.items()):
        print(k,v) ## 看看是否按照设定有序输出
        
    print("{:=^100}".format("sort by value[1], descend"))
    od2 = OrderedDict( sorted(list(d.items()), 
                             key=lambda t: t[1][1], # t[1][1]指根据value[1]排序
                             reverse = True) )
    for k,v in list(od2.items()):
        print(k,v) ## 看看是否按照设定有序输出
        
    print("原始字典占用内存大小为: %s" % sys.getsizeof(d)) # 288
    print("有序字典占用内存大小为: %s" % sys.getsizeof(od1)) # 1304
    print("有序字典占用内存大小为: %s" % sys.getsizeof(od2)) # 1304
    print("d == od1? %s" % (d == od1)) # True
    print("d == od2? %s" % (d == od2)) # True
    
# regulardict_to_ordereddict()
