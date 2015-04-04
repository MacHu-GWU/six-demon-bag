##encoding=UTF8

"""
encode, 编码, 即将str按照一定规则编为bytes
decode, 解码, 即按一定规则bytes解释为str
"""

from __future__ import print_function
from __future__ import unicode_literals

def python3_example():
    """在python3中你定义 s = "something" 的时候, 默认是utf-8编码的str
    而如果直接写入文本的时候, 如果使用w
    """
    s = "中文" # 是str
    b = s.encode("utf8") # 是bytes
    with open("test.txt", "wb") as f: # 为了保证写入文本的内容正确, 一律使用wb模式, 写入标准的二进制编码
        f.write(b)

def python3_example01():
    """在python3中定义 s = "something", 默认是utf-8编码的str。如果用"w"模式写入文件得到乱码
    """
    s = "中文"
    with open("python3_example01.txt", "w") as f:
        f.write(s)

# python3_example01()
        
def python3_example02():
    """为了让中文写入文件后不再乱码, 则要将字符串按照utf8编码成字节后再用 "wb" 写入文件
    """
    s = "中文" # 是str
    b = s.encode("utf8") # 是bytes
    with open("python3_example02.txt", "wb") as f: # 为了保证写入文本的内容正确, 一律使用wb模式, 写入标准的二进制编码
        f.write(b)

# python3_example02()

def python2_example01():
    s = "中文" # 是str, 跟当前脚本的编码等同, 只有在前面加入了u"中文"之后python才知道他是unicode
    with open("python2_example01.txt", "w") as f:
        f.write(s)
    with open("python2_example01.txt", "r") as f:
        print(f.read())
        
# python2_example01()

def python2_example02():
    s = u"中文" # 是str, 跟当前脚本的编码等同, 只有在前面加入了u"中文"之后python才知道他是unicode
    with open("python2_example02.txt", "w") as f:
        f.write(s)
    with open("python2_example02.txt", "r") as f:
        print(f.read())
        
# python2_example02()

##############
# Conclusion #
##############

"""
下面给出了在Python2和Python3中统一的对文件的读写方法。首先导入这两个
from __future__ import print_function
from __future__ import unicode_literals
"""
def write_to_file():
    """写入文件的时候, 用utf8编码写入最佳, 能保证在用浏览器打开的时候不出现乱码
    """
    s = "中文"
    with open("test.txt", "wb") as f:
        f.write(s.encode("utf8"))
        
write_to_file()

def read_from_file():
    """如果是网络上下载的文件, 可以先用chardet检测一下, 再讲decode里的内容修改为对应的编码即可
    """
    with open("test.txt", "rb") as f:
        print(f.read().decode("utf8"))
        
read_from_file()
    
    