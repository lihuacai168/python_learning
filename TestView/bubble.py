def bubble():
    arr = [33,22,11,5,1]
    # 控制循环的次数
    for i in range(len(arr)):
        # 排序,第一个需要遍历len-1,第二个(i=1)就是len-1-i,最后一个是len-1-i = 0,也就是第一个和第二比较.
        # 每排序一次,就会排好一个.所以-i就相当于减去已经排好的部分.
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print(arr)

bubble()
