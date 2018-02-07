# -*- coding: utf-8 -*-
# Authoer:Rikasai_Lee
# @Time  :2018/2/6 9:56

from functools import reduce


def prod(L):
    # reduce()里面的函数必须能接受两个参数
    return reduce(lambda x,y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
