# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author:梨花菜
# @File: 链表.py 
# @Time : 2020/3/28 20:29
# @Email: lihuacai168@gmail.com
# @Software: PyCharm

class Node:
    def __init__(self, data_val):
        self.data_val = data_val
        self.next_val = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    def list_print(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data_val)
            print_val = print_val.next_val

    def at_begin(self, new_data):
        new_node = Node(new_data)
        new_node.next_val = self.head_val
        self.head_val = new_node

    def at_end(self, new_data):
        new_node = Node(new_data)
        # 列表为空,最后一个即最后一个
        if self.head_val is None:
            self.head_val = new_node
            return

        # 遍历链表,当节点没有下一个节点时,就是最后一个节点
        laste = self.head_val
        while(laste.next_val):
            laste = laste.next_val
        laste.next_val = new_node

    def in_between(self, middle_node, new_data):
        if middle_node is None:
            print("找不到节点")
            return
        new_node = Node(new_data)
        # 新节点在原来节点的后面插入,那么新节点的下一个节点就是原来节点的下一个节点
        # 原来节点的下一个节点就是新节点
        new_node.next_val = middle_node.next_val
        middle_node.next_val = new_node

    def remove_node(self, remove_key):
        head_val = self.head_val

        # 当remove_key是头节点
        if head_val is not None:
            if head_val.data_val == remove_key:
                self.head_val = head_val.next_val
                # 清空头节点
                head_val = None
                return

        # 遍历所有节点,找到对应的remove_key就退出循环
        while head_val is not None:
            if head_val.data_val == remove_key:
                break
            prev = head_val
            head_val = head_val.next_val

        # 当循环中没找到remove_key,那么
        if head_val is None:
            return

        # head_val.data_val等于时remove_key
        # a > b > c ,删除b时,把b的下一个节点c,当成是a的下一个节点
        prev.next_val = head_val.next_val

        # 清空remove_key对应的节点
        head_val = None

list1 = LinkedList()
list1.head_val = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head_val.next_val = e2
e2.next_val = e3

list1.at_begin("Sun")
list1.at_end("Fri")

list1.in_between(list1.head_val.next_val, "Thu")
list1.remove_node("Mon")
list1.list_print()
