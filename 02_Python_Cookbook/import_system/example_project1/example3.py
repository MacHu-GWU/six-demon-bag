##encoding=utf8

"""
模块之间互相调用方法
例如我们想要在 module_name1 中调用 module_name2.add1(), 那么我们只需要在
module_name1中加上以下代码:
    from module_name2 import add1
"""

from package_name import module_name1
module_name1.print2() # 测试是否能被成功调用
