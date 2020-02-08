"""
Python中的变量都是引用式的，相当于一个存储空间的标签，而不是创建了一个盒子
"""


def show1():
    a = [1, 2, 3]
    b = a
    a.append(4)
    print(b)
    print(id(a) == id(b))


show1()
