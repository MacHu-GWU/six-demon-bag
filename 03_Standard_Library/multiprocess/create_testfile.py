##encoding=utf8

from __future__ import print_function
import os


try:
    os.mkdir("a1")
except:
    pass
try:
    os.mkdir("a2")
except:
    pass


dir_list = ["a1", "a2"]

for folder in dir_list:
    for i in range(1000):
        print(folder, i)
        res = list()
        for j in range(9999):
            res.append("a" * 100)
        with open(os.path.join(folder, str(i).zfill(4)), "w") as f:
            f.write("\n".join(res))