#!/usr/bin/python
# -*- coding: UTF-8 -*-

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        # self.parent 是为了把这个变量变成类变量，否则，parent只是局部变量
        # parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # 相当于把FooChild作为参数，然后找他的父类，也就是FooParent，然后FooParent调用init方法。
        super(FooChild, self).__init__()
        # FooParent.__init__(FooChild)
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')