# 装饰器的实现是基于闭包
login_status = False


def login(func):
    def inner():
        _username = "Rikasai"
        _password = "abc123"
        global login_status

        if login_status == False:
            username = input("please input your username")
            password = input("please input your password")

            if _username == username and _password == password:
                login_status = True
                print("login success")
            else:
                print("username or password is wrong")
        else:
            print("user already logged in")

        if login_status:
            func()  # 如果login_status = True,也就是验证通。那就过把传进来的函数再执行

    return inner


def american():
    print("--------welcome to american---------------")


def japan():
    print("--------welcome to japan---------------")


@login
def china():
    print("--------welcome to china---------------")


# 也就是给japan()加上一个login()里面的inner（）函数，但只需要执行japan就行！和@login是一样的效果
japan = login(japan)  # japan作为参数传入login，返回inner，赋值给japan；然后在执行inner（）的时候，最后执行的func()，也就是japan()

print(japan)  # <function login.<locals>.inner at 0x03A11150> 打印的是inner的内存地址,因为执行了japan = login(japan)

print(china)  # <function login.<locals>.inner at 0x02A71198> 打印的也是inner的内存地址，因为在china上面加了@login
