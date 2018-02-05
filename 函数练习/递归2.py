# 2.输入一个节点，例如：朝阳。你要遍历找，找到了就打印它，并且返回TRUE
menus = [  # 列表
    {  # 字典
        "text": '北京',
        "children": [  # 列表
            {"text": "朝阳", "children": []},  # 字典
            {"text": "昌平", "children": [  # 列表
                {"text": "沙河", "children": []},  # 字典
                {"text": "图龙观", "children": []}
            ]}
        ]
    },
    {
        "text": '广东',
        "children": [
            {"text": "深圳", "children": []},
            {"text": "广州", "children": [
                {"text": "荔湾", "children": []},
                {"text1": "番禺", "children": []}
            ]}
        ]
    }
]


#     for dict in list_father:  # 遍历父级的list，返回字典元素
#         for key in dict:  # 直接用字典来查看
#             if type(dict[key]) == list:  # 如果字典里面的一个key的values是list，就递归
#                 recursive(dict[key])
#             else:
#                 print(key, dict[key])


def recursive(list_father, find_word):
    # for dict in list_father:  # 遍历父级的list，返回字典元素
    #     for keys in dict:
    #         # print(type(dict[keys]))
    #         # print(dict.keys())
    #         # print(dict.values())
    #         if dict[keys] == "children":
    #         # if type(dict.values()) == list:
    #             return recursive(dict[keys], find_word)
    #         else:
    #             print("IF",keys, dict[keys])
    #             if dict[keys] == find_word:
    #                 return True
    #             # else:
    #             #     continue
    #         # continue
    for dict in list_father:  # 遍历父级的list，返回字典元素
        for key in dict:
            # print(dict[key])
            if dict[key] == find_word:
                # print("找到了")
                return True

            elif type(dict[key]) == list and len(dict[key]) > 0:
                if recursive(dict[key], find_word):  # 通过判断最内层递归的结果来当出口；如果直接return recursive()来递归，会导致没有递归出口
                    return True
                else:
                    continue

    return False #所有都遍历完了，没找到就返回False


# def recursive(list_father, find_word):
#     for dict in list_father:
#         # print ("遍历值：%s"%dict['text'])
#         # print ("查找值：%s"%find_word)
#         if dict['text'] == find_word:
#             return True
#         # 递归调用函数
#         elif len(dict['children']) > 0:
#             if recursive(dict['children'], find_word):
#                 count=0
#                 count+=1
#                 print(count)
#                 return True
#             else:
#                 continue
#     # else:
#     #     return None
#     return None


print(recursive(menus, "番禺"))
print(recursive(menus, "番"))
