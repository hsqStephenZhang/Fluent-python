"""
内置类型如list，dict不会调用用户定义的类覆盖的特殊方法
所以最好使用collections 模块中的UserDict,UserList，UserString来继承
"""

from collections import UserDict


class DemoDict(dict):
    def __setitem__(self, key, value):
        super(DemoDict, self).__setitem__(key,[value]*2)


class DemoDict2(UserDict):
    def __setitem__(self, key, value):
        super(DemoDict2, self).__setitem__(key,[value]*2)


def demo1():
    a=DemoDict(one=1) # 这里是不会乘以二的,因为__init__方法忽略了自己定义的__setitem方法
    a["two"]=2 # 这里是会乘以二的
    a.update(three=3)
    print(a)


def demo2():
    a = DemoDict2(one=1)
    a.update(two=2)
    print(a)


if __name__ == '__main__':
    demo1()
    demo2()