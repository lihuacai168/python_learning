# encoding: utf-8
import os
import datetime

# 字典保存有效期和端口dict_valid_day_and_sock 如：dict = {"666":"180"} 666端口的有效期是180天
dict_valid_day_and_sock = {}


def test():
    for key in dict_valid_day_and_sock:
        print("{0} valid day is {1} ".format(key,dict_valid_day_and_sock[key]))


socks_list = [824, 2078, 6667, 10086]


def ban(socks):
    for sock in socks:
        print(os.system("sudo iptables -A INPUT -p tcp --dport {0} -j DROP".format(sock)))

# 666,180表示：666端口的有效期是今天+180天

# 询问用户是否继续


def ask(func):
    def inner():
        while True:
            flag = input("do you want to continue : yes / no ")
            if flag is "y" or flag is "y":
                print("you choice {0}".format(flag))
                func()
            else:
                break
    # 装饰器返回只能返回函数名，不能带括号
    return inner


@ask
def add():
    sock = input("input sock : ")
    valid_day = int(input("input valid_day : "))
    today = datetime.date.today()
    valid_date = today + datetime.timedelta(days=valid_day)
    dict_valid_day_and_sock[sock] = valid_date


add()


