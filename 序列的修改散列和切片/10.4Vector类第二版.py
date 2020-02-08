"""
为了支持切片，我们只需要实现__len__,__getitem__方法即可
"""

from array import array
import numbers
import reprlib
import math


class Vector(object):
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):  # 返回一个迭代器
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __hash__(self):
        result = 0
        for item in self._components:
            result = result ^ hash(item)  # 简单的异或还不完善
        return result

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self._components))  # 欧氏距离的函数

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]
        # 这样实现的切片的结果不是我们想要的Vector类的实例，而是一个list


class Vector2(Vector):
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            raise TypeError("Wrong input")


if __name__ == '__main__':
    v1 = Vector([3, 4, 5, 6, 7, 8, 9, 10])
    v2 = Vector2([1, 2, 3, 4, 5, 6, 7])
    v3 = v1[1:3]
    v4 = v2[1:3]  # 在Vector2中的__getitem__方法构造了新的实例
    print(type(v3), type(v4))
