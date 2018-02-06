# -*- coding: utf-8 -*-
# Authoer:Rikasai_Lee
# @Time  :2018/2/6 9:56

from functools import reduce


def prod(L):
    # for i in L:
    #     print("inner+%s"%i)
    # product = 1
    # for i in L:
    #     product = product * i
    # return product
    return reduce(lambda x,y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
