

#匿名函数练习
# func = lambda x,y:x-y if x>y else x+y #先写参数，然后分号: 接着写条件成立执行的语句(三目运算)
# print(func(3,2))

#匿名函数配合map使用

# print(map(lambda x:x*x,range(10))) #map需要变成list对象才能被输出 range()这个位置是一个或可迭代的参数
print(list(map(lambda x:x*x,range(10))))