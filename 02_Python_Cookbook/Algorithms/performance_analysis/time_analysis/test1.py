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

@profile
def test1():
    a = [i for i in range(10000)]
    isin_list = list()
    for i in a:
        isin_list.append(i in a)
    return isin_list

@profile
def test2():
    a = set([i for i in range(10000)])
    isin_list = list()
    for i in a:
        isin_list.append(i in a)
    return isin_list

if __name__ == "__main__":
    isin_list = test1()
    isin_list = test2()