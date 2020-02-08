"""
Python尽量支持基本协议

对于一个序列来说，协议要求其实现__getitem__,__contains__,__iter__,__reversed__
index,count的方法
但是，鉴于序列的重要性，在类没有实现__contains__和__iter__方法的时候，只需要定义了
__getitem__方法，也可以实现in,和迭代运算符
"""


class Func(object):
    def __init__(self):
        self.data = range(0,20,2)

    def __getitem__(self, item):
        return self.data[item]


if __name__ == '__main__':
    func=Func()
    print(1 in func.data)
    for i in func.data:
        print(i,end=" ")
