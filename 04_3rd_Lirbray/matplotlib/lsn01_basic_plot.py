##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-16

""" 基本画图说明: [颜色][线型][标记]"""

from __future__ import print_function
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

def example1():
    """ 1. [颜色]
    有三种方法可以选择颜色：
    方法1: 直接选择预定义的颜色
        plt.plot(x, y, color = "b")
        b: blue 蓝色
        g: green 绿色
        r: red 红色
        c: cyan 青绿色
        m: magenta 洋红
        y: yellow 黄色
        k: black 黑色
        w: white 白色
    方法2: 对于灰度图像
        plt.plot(x, y, color = "0.75") # 值在0-1之间
    方法3: HTML 16进制字符串
        plt.plot(x, y, color = "#eeefff") # 请查阅HTML相关文档
    方法4: RGB tuple
        plt.plot(x, y, color = (0.25, 0.5, 0.75)) # R,G,B值都在0-1之间
    """
    plt.plot(x, y, "r") # 颜色
    plt.show()

# example1()

def example2():
    """ 2. [线型]
    方法:
        plt.plot(x, y, "-。")
    所有的选项如下:
        "-" (solid) – default 
        "--" (dashed) 
        "-." (dash dot) 
        ":" (dotted) 
        "None" or " " or "" (nothing) 
    下面这段代码可以显示所有的线型选项
        from matplotlib.lines import Line2D
        print Line2D.lineStyles.keys()
    """
    plt.plot(x, y, "--") # 线型
    plt.show()

# example2()

def example3():
    """ 3. [标记]
    方法:
        plt.plot(x, y, "o") # 标记
    所有的选项如下:
        [0, 1, 2, 3, 4, "D", 6, 7, "s", "|", "", 
        "None", None, "x", 5, "_", "^", " ", "d", 
        "h", "+", "*", ",", "o", ".", "1", "p", 
        "3", "2", "4", "H", "v", "8", "<", ">"]
    下面这段代码可以显示所有的标记选项
        from matplotlib.lines import Line2D
        print Line2D.markers.keys()
    """
    plt.plot(x, y, "^") # 标记
    plt.show()

# example3()

def example4():
    """ 如何同时定义 [颜色][线型][标记] """
    plt.plot(x, y, "r-.o") # 方法1, 格式字符串
    plt.plot(x, y, color = "r", linestyle = "-.", marker = "o") # 方法2, 分别定义
    plt.plot(x, y, color = "r", linestyle = "-.", marker = "o", # 方法3, 定义粗细，大小
             linewidth = 5, markersize = 10) # 线条粗细， 标记大小
    plt.show()

# example4()