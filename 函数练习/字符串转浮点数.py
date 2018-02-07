# -*- coding: utf-8 -*-
# Authoer:Rikasai_Lee
# @Time  :2018/2/6 16:50

from functools import reduce

DIGITS = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7":7,"8":8,"9":0,"0":0}


def str2float(s):
    # 找到小数点的位置
    dot = s.find(".")

    # 字符串转换成数字
    def str2num(s):
        return DIGITS[s]

    # 数字转换成浮点数
    def float(x, y):
        return x * 10 * 1.0 + y

    # 小数点之前的字符串
    dot_before_list = list(map(str2num, s[0:dot]))

    # 小数点之后的字符串
    dot_behind_list = list(map(str2num, s[dot + 1:]))

    # 小数点之前的字符串转成浮点数
    dot_before = reduce(float, dot_before_list)

    # 小数点之前的字符串转成浮点数
    dot_behind = reduce(float, dot_behind_list) / (10 ** len(dot_behind_list))

    return (dot_before + dot_behind)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
