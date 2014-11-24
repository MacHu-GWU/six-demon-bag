##encoding=utf8

from __future__ import print_function
from HSH.Data.js import load_js, dump_js, prt_js
import cjson
import time
import random
import sys
# print(dir(cjson))

def rand_string(length):
    """highest performance non-dependent pure python random string generator
    """
    # All the characters you want to use in your strings:
    test_chars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([random.choice(test_chars) for i in range(length)])

data = {str(i) : {rand_string(32): list(range(500)) for j in range(100)} for i in range(1000)}
print(sys.getsizeof(data))
# dump_js(data, "data.json", fastmode = True, replace = True)
# load_js("data.json")
st = time.clock()
with open("test.json", "w") as f:
    f.write(cjson.encode(data))
print(time.clock() - st)


# st = time.clock()
# with open("test.json", "r") as f:
#     cjson.decode(f.read())
# print(time.clock() - st)