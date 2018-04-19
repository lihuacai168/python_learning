# -*- coding: utf-8 -*-
# 在下面的代码中，将实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance。
class Singleton(object):
    _instance = None
    def __new__(cls,*args,**kw):
        print("This is Singleton Class")
        if not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1
# a = Child()