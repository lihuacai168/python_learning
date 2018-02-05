

# def calc(n):
#         n = int(n/2)
#         if n > 0.1:#递归出口
#             print(n)
#             calc(n) #调用函数本身
#         print(n)
# calc(10)

menus = [ #列表
    {#字典
        "text":'北京',
        "children":[#列表
            {"text":"朝阳","children":[]},#字典
            {"text":"昌平","children": [#列表
                {"text": "沙河", "children": []},#字典
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
                {"text": "番禺", "children": []}
            ]}
        ]
    }
]
#1.遍历所有的节点
#2.输入一个节点，番禺。你要遍历找，找到了就打印它，并且返回TRUE，没有找到就说不存在
# def recursive_search(list):
#     for dic in list:#第一层遍历列表，返回dic
#         print("这个是list里面的字典",dic)
#         for list_second in dic:#第二层遍历，返回list
#             if list_second == None:
#                 break
#             else:
#                 print("这个dic字典里面的",list_second)
#                 recursive_search(list_second)
def recursive_search(list):
    for dic in list:#第一层遍历列表，返回dic
        # recursive_search(dic)
        if dic["text"] == "番禺":
            return dic
        else:
            if len(dic["children"])> 0:
                recursive_search(dic["children"])
    print('不存在')

result = recursive_search(menus)
print(result)