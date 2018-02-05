# 5.请删除字典中键值对'k1','v1',并输出删除后的字典
# dic2 = {'k1':'v1','k2':'v2','k3':'v3','a':'b'}
# dic2.pop("k1")
# for k in dic2:
#     print(k,dic2[k])

# 6.请删除字典中的键’k5'对应的键值对,如果字典中不存在键’k5',则不报错,并且让其返回None.
def del_key():
    dic2 = {'k1':'v1','k2':'v2','k3':'v3','a':'b'}
    if dic2.get("k5"):
        dic2.pop("k5")
    else:
        return None

