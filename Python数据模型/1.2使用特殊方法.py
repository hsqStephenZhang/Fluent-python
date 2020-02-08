"""
特殊方法的存在是为了Python解释器使用的，自己并不需要使用
比如不存在deck.__len__()这种写法，自己用的时候只需要用len()即可
Python会调用__len__()这种方法
对于内置的类型，CPython会直接调用类型的ob_size属性来求其长度，比调用该函数要快得多

对于 for i in x:这个语句，其实是使用了iter(x)的方法，其背后调用的是__iter__()方法
"""
import math


class Vector(object):
    """
    自定义简单的向量类
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # 或者 __repr__也是可行的
        """
        如果没有自定义该函数，print一个实例的时候就只可能是:
        <Vector object at 0x10e10070>
        """
        return "[Vector(%r,%r),dtype='%r']" % (self.x, self.y, type(self.x))

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)  # 返回一个新的向量

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)


if __name__ == '__main__':
    v = Vector(1, 3)
    u = Vector(2, 4)
    print(v.__doc__)  # 描述类信息，可以被自动收集
    print(u * 5)
    print(u - v)
