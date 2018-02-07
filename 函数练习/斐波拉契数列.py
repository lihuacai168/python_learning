# -*- coding: utf-8 -*-
# Authoer:Rikasai_Lee
# @Time  :2018/2/6 15:28

# 对应的位置：  1 2 3 4 5 6 7  8  9
# 斐波拉契数列：1 1 2 3 5 8 13 21 34

# def fb(max):
#     # n计算次数，a是数列的第一个，b是第二个
#     n, a, b = 0, 0, 1
#     while n < max:
#         if max == 1:
#             return b
#         else:
#             a, b = b, a + b
#         # return fb(max)
#         n = n + 1
#     return a
# print(fb(1))

# 列表生成式

def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b #返回b，并把函数的执行位置冻结在这里
        a, b = b, a + b
        n = n + 1
print(list(fib(2)))