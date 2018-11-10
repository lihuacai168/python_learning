# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 16:20
# @Author  : Rikasai
# @Email   : lihuacai168@gmail.com
# @File    : quick_search.py
# @Software: PyCharm

# 二分法找出有序递增数组,第一个重复元素的索引
def quick_search(arr,find_word):
    # 数组的开始和最后一个游标
    first = 0

    last = len(arr) - 1

    if find_word in arr:

            while True:
                    # 取数组的中间值
                    mid = int((first + last)/2)

                    if arr[mid] == find_word and arr[mid-1] < find_word:
                        print(str(find_word)+" index is: "+str(mid))
                        return mid

                    # 要找的值小于中间值,也就是在左边.即下一次查找时是arr[0:mid-1]的的区间
                    elif find_word <= arr[mid]:
                        if arr[first] == find_word:
                            print(str(find_word) + " index is: " + str(first))
                            return first
                        last = mid-1

                    # 要找的值大于中间值,也就是在右边.即下一次查找时是arr[mid+1:last]的的区间
                    elif find_word > arr[mid]:
                        first = mid+1

    else:
        print("not in arr")

# arr是升序,递增的数组.含有重复的值
arr = [1,1]
quick_search(arr,1)









