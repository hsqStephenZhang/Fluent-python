"""
Python的一元运算符有+,-,~,abs等
对于之前的Vector,这里实现几个方法

对于运算符来说，始终返回一个新的对象，而不是在原来的对象基础上修改
"""

from array import array
import numbers
import reprlib
import math


class Vector(object):
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(x for x in self)

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
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            raise TypeError("Wrong input")


if __name__ == '__main__':
    v1 = Vector([1, 2, 3])
    v2 = -v1
    v3 = +v1
    print(id(v1))
    print(id(v2))
    print(id(v3))  # v1,v2,v3's id are different at all
