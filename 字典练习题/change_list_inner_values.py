# lis = [['k',['qve',20,{'k1':['tt',3,'1']},89],'ab'l]
# 。
# 1.将列表lis 中的'tt'变成大写(用两种方式)。

# lis = [['k',['qve',20,{'k1':['tt',3,'1']},89],'ab']]
# # lis[0][1][2]["k1"][0] = "TT" #第一种方法
#
# # 第二种方法
# for k in lis:#第一重循环，['k',['qve',20,{'k1':['tt',3,'1']},89],'ab']
#     # print(k)
#     for k1 in k:#第二重循环，['qve',20,{'k1':['tt',3,'1']},89]
#         # print(k1)
#         for k2 in k1:#第三重循环，{'k1':['tt',3,'1']}
#             # print(type(k2))
#             if type(k2) == dict :
#                 k2["k1"] = "TT"
#                 print(k2["k1"])


# 2.将列表中的数字3 变成字符串'100'(用两种方式).
# lis = [['k',['qve',20,{'k1':['tt',3,'1']},89],'ab']]
# for k in lis:#第一重循环，['k',['qve',20,{'k1':['tt',3,'1']},89],'ab']
#     # print(k)
#     for k1 in k:#第二重循环，['qve',20,{'k1':['tt',3,'1']},89]
#         # print(k1)
#         for k2 in k1:#第三重循环，{'k1':['tt',3,'1']}
#             # print(type(k2))
#             if type(k2) == dict and k2.get('k1'):
#                 last_list = k2.get('k1') #last_list 是['tt',3,'1']
#                 for index,value in  enumerate(last_list):
#                     if value == 3:
#                         last_list[index] = "3"
#                         print(last_list[index])




# 3.将列表中的字符串'1'变成数字101(用两种方式)。

