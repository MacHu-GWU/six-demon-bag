##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function

""" ============= PROBLEM description ============ 
[Chn]许多时候，我们希望class的某些属性不仅仅是数值，而且也是对象。
    这样我们就可以用 class.属性.方法 来调用子类中的方法了
"""

class AK(object):
    def __init__(self):
        self.armo = Armo(30)
        
    def shoot(self):
        self.armo.num -= 1

class Armo(object):
    def __init__(self, num):
        self.num = num
        
    def __str__(self):
        return "%s bullets left" % self.num
    
    def clear(self):
        self.num = 0
        
    def reload(self):
        self.num = 30
        
ak = AK()
print("初始化ak之后, %s" % ak.armo)

ak.shoot()
print("开了一枪之后, %s" % ak.armo)

ak.armo.clear()
print("清空子弹之后, %s" % ak.armo)

ak.armo.reload()
print("重新装弹之后, %s" % ak.armo)