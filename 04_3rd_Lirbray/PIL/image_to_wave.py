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

def expand_window(center, window_size, max):
    """
    index is from 0 to max - 1
    """
    if center - window_size < 0:
        lower = 0
    else:
        lower = center - window_size
    if center + window_size + 1 > max:
        upper = max
    else:
        upper = center + window_size + 1
    return np.array(range(lower, upper))

# print(expand_window(98, 3, 100))

def img_to_wav(path, max_x, max_y, window_size = 2):
    """
    [Args]
    ------
    path: the image file path, absolute path
    
    max_x: the x axis is from 0 - max_x, float type
    
    max_y: the y axis is from 0 - max_y, float type
    
    window_size: margin smooth sampling window size, int type
    
    [Return]
    --------
    x, y value
    """
    im = Image.open(path).convert("L")
    data = np.array(im)[::-1] # python中图是从上到下的。为了让index是从下到上的，所以要逆序输出
    
    resolution_x, resolution_y = max_x/data.shape[1], max_y/data.shape[0]

    x, y = list(), list()
    
    for i in range(data.shape[1]):
        window = expand_window(i, window_size, data.shape[1])
        margin_dots_y_indices = np.where(data[:, window] == 0)[0]
        
        if len(margin_dots_y_indices) > 0: # if found at least one dots in margin
            x.append((i+1) * resolution_x)
            y.append(margin_dots_y_indices.mean() * resolution_y)
            
    return np.array(x), np.array(y)

if __name__ == "__main__":
    from matplotlib import pyplot as plt
    x, y = img_to_wav(r"images\wave_a1.png", 10.0, 100.0)
    plt.plot(x, y)
    plt.show()

    
    
