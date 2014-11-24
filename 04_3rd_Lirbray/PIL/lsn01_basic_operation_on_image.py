##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-10             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function
from PIL import Image
import numpy as np

def example1():
    """下采样，压缩尺寸
    """
    im = Image.open(r"images\wave_a1.png")
    im.thumbnail((1920, 1080),Image.ANTIALIAS)
    im.save(r"images\wave_a2.png")
    
# example1()

def example2():
    """转灰度图像
    """
    im = Image.open(r"images\wave_b1.png")
    im = im.convert("1") # 1 = 0, 255 纯黑白模式， L = 0-255黑白模式， RGB = 彩色模式
    im.save(r"images\wave_b2.png")

# example2

def example3():
    """ image to array, array to image
    """
    im = Image.open(r"images\wave_a1.png")
    im = im.convert("L") # for grayscale, make sure the mode is right
    data = np.array(im) # image to array
    print(data)
    
    im1 = Image.fromarray(data) # array to image
    im1.show()
    
# example3()
