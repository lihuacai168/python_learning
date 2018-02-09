# -*- coding: utf-8 -*-
# Authoer:Rikasai_Lee
# @Time  :2018/2/9 11:12

import os, json,sys


def word_location(find_word):
    # 员工表的字段在列表中的位置
    staff_field_dict = {"staff_id": 0, "name": 1, "age": 2, "phone": 3, "dept": 4, "enroll_date": 5}

    for k in staff_field_dict:
        if k == find_word:
            print("执行了word_location")
            return staff_field_dict[k]
    else:
        return False


def get_operation(operation):
    # 操作类型
    operation_dict = {"=": "equal", ">": "bigger", "<": "smaller", "like": "like"}

    for k in operation_dict:
        if k == operation:
            print("执行了get_operation")
            return operation_dict[k]
    else:
        return False

def get_staff_table_list():
    if os.path.isfile("staff.json"):

        # 读取员工表
        f = open("staff.json", mode="r")

        # 输出当前函数名
        print("执行了"+sys._getframe().f_code.co_name)

        # 把员工表转换成list
        list_staff_table = json.load(f)

        # 关闭文件流
        f.close()

        return list_staff_table



    else:
        print("木有员工表哦，先去添加员工表")
        return False

def equal(find_word,find_word_value,find_word_location,list_staff_table):
    # 输出当前函数名
    print("执行了" + sys._getframe().f_code.co_name)

    list_equal = []

    for list_inner in list_staff_table:

        print("遍历了员工表")
        # print(list_inner)

        if find_word_value == list_inner[find_word_location]:
            list_equal.append(list_inner)
            print(list_equal)



def find_staff(find_word,operation,find_word_value,*seclect_word):

    # 查找字段在员工列表的位置
    find_word_location = word_location(find_word)

    # 给操作类型赋值
    _operation = get_operation(operation)

    if find_word_location == False:
        print("查找的字段不存在哦")
    else:
        list_staff_table = get_staff_table_list()
        l=equal(find_word,find_word_value,find_word_location,list_staff_table)
        print(l)



        # 初始化保存查找结果的列表
        # list_find = []
        #
        # if os.path.isfile("staff.json"):
        #
        #     # 读取员工表
        #     f = open("staff.json", mode="r")
        #
        #     print("打开了文件")
        #     # 把员工表转换成list
        #     list_staff_table = json.load(f)
        #
        #     # 遍历员工表list
        #     for list_inner in  list_staff_table:
        #
        #         print("遍历了员工表")
        #         # print(list_inner)
        #
        #         if find_word_value==list_inner[find_word_location]:
        #             list_find.append(list_inner)
        #             print(list_find)


        # else:
        #     print("木有员工表哦，先去添加员工表")

find_staff("dept","=","it",["name","age"])

# s =read_staff_table()
# print(s)
