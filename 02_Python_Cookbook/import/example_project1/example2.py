##encoding=utf8

"""
通常我们调用模块中的方法是采用如下代码实现的
    import package_name.module_name
    package_name.module_name.method_name()

而有时候我们想要直接通过 package_name.method_name 来直接调用方法, 而省略了module_name这一栏
那我们就必须在 package_name 下的 __init__.py 文件中添加:
    from .module_name import method_name

然后我们在调用时就可以直接:
    import package_name
    package_name.method_name()
或:
    from package_name import *
    method_name()
"""

import package_name
package_name.print1()

from package_name import *
print1()