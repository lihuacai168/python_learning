# 编写一个闭包实例

def outer():
    print("this is outer")

    def inner():
        print("this is inner")

    return inner  # 外层函数outer return 内层函数 inner的函数名字，不带括号，所以inner函数不会执行


outer()#调用外层函数只会执行自己的print，不会自行inner的print

closure = outer() #把outer的返回值赋给closure，相当于closure = inner，赋值时，outer被执行一次了

closure() #调用closure()，相当于调用 inner();直接在外部执行outer函数的内部函数inner，这个就是闭包 



