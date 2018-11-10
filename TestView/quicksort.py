def quick_sort(list,first,last):

    # 只有一个元素时,就是递归的出口
    if first >= last:
        return

    # 数组的游标
    low = first
    high = last

    # 去数组的第一个值作为参照
    mid_value = list[first]

    while low < high:

        # 如果高位的值大于参照的值并且游标还没相遇,高位游标就一直向左移动.(高位的值等于参照值,也需要移动,否则当数组的前后两个元素刚好相等,会出现死循环)
        if low < high and list[high] >= mid_value:
            high -= 1

        # 退出遍历时,要是高位的值小于参照的值,就放在低位去.要是游标相等时,也进行赋值(两个空值赋值,不会影响).但low+=1放到下一步去操作,还要进行判断low和high的大小.再把低位的游标向右移动,避免出现low>high的情况.
        list[low] = list[high]

        # 如果低位的值小于参照的值并且游标还没相遇,低位游标就一直向右移动
        if low < high and list[low] < mid_value:
            low += 1

        # 退出遍历时,和high的一样
        list[high] = list[low]

    # 退出遍历时,游标low和high是相等的,也就是mid_value的游标
    list[low] = mid_value

    quick_sort(list,0,low-1)
    quick_sort(list,low+1,last)

num = [4,7,1,-2,6,3,2,3,90,2,4]

quick_sort(num,0,len(num)-1)

print(num)