

#格式输出
name = input("input Name: ")
age = input("input Age: ")
job = input("input Job: ")
info = """
======== Message of %s   ========
======== Name :  %s       ========
======== Age  :  %s       ========         
======== Job  :  %s       ========
"""%(name,name,age,job)
print(info)
