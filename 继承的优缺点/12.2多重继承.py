"""
多重继承就是一个按照MRO(Method Resolution Order)方法解析顺序
它是按照广度优先的顺序继承的，继承的时候按照class的__mro__列表的顺序继承
找到当前类的下一个父类，判断是否有该方法
可以在super()的参数中直接指定要从mro列表的哪一个类开始搜索
"""


class B(object):
    def ping(self):
        print("this is {}".format(self.__class__))


class C(B):
    def ping(self):
        super(C, self).ping()
        print("this is in class C")


class D(B):
    def ping(self):
        super(D, self).ping()
        print("this is in class D")


class E(C,D):
    def ping(self):
        super(C, self).ping()
        print(E.__mro__)


if __name__ == '__main__':
    b=B()
    c=C()
    d=D()
    e=E()
    e.ping()