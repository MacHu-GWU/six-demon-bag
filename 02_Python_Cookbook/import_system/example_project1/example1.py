##encoding=utf8

"""
导入模块中的方法

方法1, import 包.模块, 再用 包.模块.方法
import package_name.module_name1 as module_name1
module_name1.print1()

方法2, from 包.模块 import 方法
from package_name.module_name1 import print1
print1()
"""

import package_name.module_name1 as module_name1
module_name1.print1()

from package_name.module_name1 import print1
print1()
