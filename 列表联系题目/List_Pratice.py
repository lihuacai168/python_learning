# 打印出列表的每个元素和索引
# names=["caijian","Rikasai","xiyan","sunjian","花菜"]
# for index,name in enumerate(names):
#     print(index,name)

# 打印出列表的每个元素和索引,当索引为偶数时，把对应的元素改成-1
# names=["caijian","Rikasai","xiyan","sunjian","花菜"]
# for index,name in enumerate(names):
#     print(index,name)
#     if index%2 == 0:
#         names[index] = -1

# names列表中有3个2，动态返回第二个2索引,和它的值
# names = ["caijian",2,"Rikasai","xiyan","sunjian",2,"花菜",2]
# index_first = names.index(2)#第一个2的索引
# names_new = (names[index_first + 1:])#第二个2应该去掉除第一个2之后的列表开始找，所以应该用index_first+1开始查找
# index_second = names_new.index(2)#第二个2在新列表的索引
# second_val = names[index_first+index_second+1]
# print(second_val)

# 商品列表如下：
# products =[["iphone8",6888],["MacPro",12888],["小米",3888],["book",88],["Nike shoe",888],]
# 写一个循环，不断地问用户想买什么，用户选择一个商品编号，就把对应添加到购物车里面，用户输入q则退出，打印购物车的商品列
products = [["iphone8", 6888], ["MacPro", 12888], ["小米", 3888], ["book", 88], ["Nike shoe", 888]]
shopping_cart = []
exit_flag = False
while not exit_flag:
    print("--------------商品列表------------")
    for index, p in enumerate(products):  # 列表中有列表，可用枚举enumerate来循环，方便取出子列表的值
        print("%s.    %s     %s" % (index, p[0], p[1]))
    uesr_input = input("请输入你想买商品的编号：")
    if uesr_input.isdigit():
        if int(uesr_input) >= len(products):
            print("商品不存在")
        elif int(uesr_input) >= 0:
            print("已经把%s加入购物车" % products[int(uesr_input)])
            shopping_cart.append(products[int(uesr_input)])
            print("--------------商品列表------------")
        # else: didigit方法不能判断负数
        #     print("商品编码不能为负数")
    elif uesr_input == "q":  # 输出的字符为q则退出
        if len(shopping_cart) > 0:
            print("--------------商品列表------------")
            for index, p in enumerate(shopping_cart):
                print("%s.    %s     %s" % (index, p[0], p[1]))
        exit_flag = True
    else:
        print("%s不是正确商品编码，请重新输入" % uesr_input)
        continue
