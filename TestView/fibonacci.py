# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 18:10
# @Author  : Rikasai
# @Email   : lihuacai168@gmail.com
# @File    : fibonacci.py
# @Software: PyCharm
# 1,1,2,3,5,8
def fibonacci(n):
    list_ = [1,1]
    if n == 1 or n== 2:
        print("前两项都是1")
        return list_
    else:
        first = 1
        second = 1
        # 第n项等于前两项之和.从第三项开始计算.也就是说i=0时,计算出来是n=3的值.要用range(n-2).
        for i in range(n-2):
                first,second = second,first+second
                list_.append(second)
                 # temp = second
                 # second = first + second
                 # first = temp
        return list_

def fibonacci_while(n):
    i, a, b = 0, 0, 1
    L = []
    while i<n:
        a, b = b, a+b
        i += 1

        # 退出循环时,a已经被b赋值.
        L.append(a)
    return L

print(fibonacci_while(20))

# print(fibonacci(1))