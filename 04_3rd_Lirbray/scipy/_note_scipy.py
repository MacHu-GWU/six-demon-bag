##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

import numpy as np
from scipy.stats import itemfreq

hist = itemfreq([40,30,30,20,20,20,10,10,10,10]) ## freq
print hist

hist = np.float32(hist)
print hist
d = np.array([1.2,3.2])
print d.astype('int')
# y = hist.view('float32')
# y[:]=hist

# hist_T = hist.transpose()
# hist_T[1] = hist_T[1] / 100.0
# print hist_T.transpose()
# import scipy.misc as sc
# print sc.comb(5, 3)