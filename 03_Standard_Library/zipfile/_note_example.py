##encoding=utf8
from zipfile import ZipFile
import os

def initial_test_files():
    """创建初始数据
    """
    try:
        os.mkdir("test")
    except:
        pass
    with open("doc1.txt", "w") as f:
        f.write("123")
    with open(r"test\doc2.txt", "w") as f:
        f.write("abc")
        
def see_how_it_works():
    """展示zipfile.ZipFile的各种行为
    1. 压缩当前目录的文件
    2. 压缩当前目录
    3. 压缩其他目录下的文件
    4. 只压缩文件, 不压缩目录
    """
    with ZipFile("z1.zip", "w") as myzip:
        myzip.write(r"doc1.txt")
    with ZipFile("z2.zip", "w") as myzip:
        myzip.write(r"test")
    with ZipFile("z3.zip", "w") as myzip:
        myzip.write(r"test\doc2.txt")
        
    with ZipFile("z4.zip", "w") as myzip:
        os.chdir("test")
        myzip.write(r"doc2.txt")
        
initial_test_files()
see_how_it_works()