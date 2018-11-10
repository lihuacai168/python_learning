# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 16:20
# @Author  : Rikasai
# @Email   : lihuacai168@gmail.com
# @File    : quick_search.py
# @Software: PyCharm

def quick_search(arr,find_word):
    # 数组的开始和最后一个游标
    first = 0

    last = len(arr) - 1

    if find_word in arr:

        # 最后一个元素需要判断,因为mid = int((first + last)/2)永远取不到最后一个值
        if find_word == arr[-1]:
            print(str(find_word) + " index is: " + str(last))

        else:
            while True:
                    # 取数组的中间值
                    mid = int((first + last)/2)

                    if arr[mid] == find_word:
                        print(str(find_word)+" index is: "+str(mid))
                        return mid

                    # 要找的值小于中间值,也就是在左边.即下一次查找时是arr[0:mid]的的区间
                    elif find_word < arr[mid]:
                        last = mid

                    # 要找的值大于中间值,也就是在右边.即下一次查找时是arr[mid:last]的的区间
                    else:
                        first = mid

    else:
        print("not in arr")

# arr是升序,且不重复的数组
arr = [0,1,2,13,67,100,188]
quick_search(arr,67)









