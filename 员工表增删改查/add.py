# -*- coding: utf-8 -*-
# Authoer:Rikasai_Lee
# @Time  :2018/2/7 13:48

# 员工表字段
"""
staff_id name          age phone            dept enroll_date
1        Rikasai Lee    22 186661236234     IT   2016-06-14
"""
import datetime

# 初始化员工表
staff_table = []


# 判断电话号码是否已经在存在员工表
def check_phone(phone):
    # global staff_table
    for list in staff_table:
        if list[3] == phone:
            return True
        else:
            # return False
            continue


def add_staff():
    # 本次新增加到staff_table的元素位置
    start_list = len(staff_table)

    # 注册日期
    enroll_date = datetime.datetime.today().strftime("%Y-%m-%d")

    # 记录操作的员工条数
    count = 0

    while True:

        # 员工表为空，那第一个员工的staff_id = 1,否则就是最后一个员工的staff_id + 1
        if len(staff_table) > 0:
            staff_id = staff_table[-1][0] + 1
        else:
            staff_id = 1

        name = input("请输入员工的名字:")
        age = input("请输入员工年龄:")
        phone = input("请输入员工的电话:")

        # 检测手机号码是否存在
        while check_phone(phone):
            phone = input("该号码已经存在，请输入新的号码:")
        # phone=check_phone(phone)

        dept = input("请输入员工的部门:")

        # 把输入的信息保存在staff_list
        staff_message = [staff_id, name, age, phone, dept, enroll_date]
        staff_table.append(staff_message)

        count += 1

        continue_input = input("\n请问是否继续增加,y or n:\n").lower()
        if continue_input == "y":
            continue
        else:
            break
    print("\n本次增加%s名员工:"%count)
    for i in staff_table[start_list:]:
        print(i)

add_staff()
