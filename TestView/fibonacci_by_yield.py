# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 19:03
# @Author  : Rikasai
# @Email   : lihuacai168@gmail.com
# @File    : fibonacci_by_yield.py
# @Software: PyCharm

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
# fab(2)
for i in fab(2):
    print(i)

