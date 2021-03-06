"""
本章主要是说明用于生成对象表示形式的众多方法
"""

from array import array
import math


class Vector2D(object):
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):  # 返回一个迭代器
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "<{}({!r},{!r})>".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)  # 欧氏距离的函数

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls,octets):
        typecode=chr(octets[0])
        memv=memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 1)
    print(v1)
    print(abs(v1))
    print(bytes(v1))
    print(str(v1), repr(v1))
    print(v2.frombytes(bytes(v1)))

