

#列表的用方括号表示
classmates = ['Michael', 'Bob', 'Tracy']

#列表里面的元素可以是列表
s = ['python', 'java', ['asp', 'php'], 'scheme']

#查看列表的长度用len()
print(len(classmates))

#删除列表的元素用pop()
classmates.pop(1)

#元组，和list列表很像，用小括号表示
t = (1,)#Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

#元组tuple是不可以变的，但是如果元素是list时，这个元素里面的内容是可以变的
t2 = ('a', 'b', ['A', 'B'])
