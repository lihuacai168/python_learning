# -*- coding: utf-8 -*-
import datetime,os

# dict for sock and date
dict = {}


# 输入需要禁用的端口和日期
def my_input():
    socks = input("please input sock that need to be banned:")
    date = input("please input validity period for the sock:")
    save(socks, date)


# save sock as key,date as value to dictionary
def save(socks, add_date):
    for sock in socks.split(","):
        delta = datetime.timedelta(days=int(add_date))
        today = datetime.date.today()
        valid_day = today + delta
        dict[sock] = valid_day


def ban():
    print("ban begin:")
    for sock in dict:
        if dict[sock] > datetime.date.today():
            os.popen("sudo iptables -A INPUT -p tcp --dport %s -j DROP"%dict[sock])
            print("ban execute")


def ban_log():
    pass


if __name__ == "__main__":
    go = input('do you wanna continue: yes or no')
    if go == 'y' or go == 'yes':
        my_input()
    ban()
