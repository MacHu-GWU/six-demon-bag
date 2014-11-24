##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-16

"""
画较为复杂的图，对下面的元素进行自定义：
    1. 子图
    2. axis
    3. axis label
    4. title
    5. legend
    6. grid
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

def example1():
    """matplotlib和matlab画图类似，抽象概念上从上到下分别是:
    plt.figure()
        |--- plt.subplot()
            |--- plt.axis()
            |--- plt.set_title()
            |--- plt.set_xylabel()
            |--- plt.legend()
            |--- plt.grid()
    """
    x = np.linspace(1, 10, 10)
    Y = np.random.randn(4, 10)

    f = plt.figure() # 定义figure画板
    f.suptitle("3 line in 1 plot", fontsize=14, fontweight="bold") # 定义画板的总标题
    
    for y, i in zip(Y, range(2 * 2)):
        sbplt = plt.subplot(2, 2, i + 1) # 定义 subplot
        
        plt.plot(x, y, label = "y%s = x" % i)
        
        plt.axis([1, 10, -3, 3]) # 定义 axis坐标轴
        plt.xticks(np.arange(1, 10.1, 1) )
        plt.yticks(np.arange(-3, 3, 1) )
        
        sbplt.set_title("y%s = f(x)" % i) # 子图的总标题
        sbplt.set_xlabel("x axis") # 子图的 x axis label
        sbplt.set_ylabel("y axis") # 子图的 y axis label
        
#         plt.legend(loc="center left", bbox_to_anchor = (1, 0.5) ) # 图例在右边
        plt.legend(loc="upper center", bbox_to_anchor = (0.5, 1) ) # 图例在上面
        plt.grid()
        
    plt.show()
    
# example1()

def example2():
    """在图表上写上注释和文字
    """
    x, y, label = np.random.randn(5), np.random.randn(5), np.array([1, 1, 0, 0, 1])
    
    plt.plot(x, y, "o")
    plt.axis([-3, 3, -3, 3])
    for i, j, c in zip(x, y, label):
        plt.text(i, j, "%s" % c, fontsize=15) # 在 x=i, y=j的位置上显示文字
    plt.annotate('look at here!', # 箭头文字
                 xy=(i, j), # 指向x=i, y=j的位置
                 xytext=(i+0.5, j+0.5), # 箭头是从哪里指向
                 arrowprops=dict(facecolor='black', # 箭头的颜色
                                 shrink=0.05) ) # 箭头的粗细
    plt.show()
    
# example2()