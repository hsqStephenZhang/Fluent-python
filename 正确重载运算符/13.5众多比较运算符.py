"""
Python的一元运算符有+,-,~,abs等
对于之前的Vector,这里实现几个方法

对于运算符来说，始终返回一个新的对象，而不是在原来的对象基础上修改


对于中缀运算符来说，反向的方法是为了处理类型不同的操作数
"""

from array import array
import numbers
import reprlib
import math
import itertools
from collections import abc


class Vector(object):
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(x for x in self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            print("add func called")
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented  # 因为add方法的两个操作数发生了TypeERROR之后，
            # 仍然有可能调用radd返回正确结果，而如果此时反悔了TypeError，那么就直
            # 接返回失败了

    def __radd__(self, other):
        print("radd func called")
        return other + self

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            print("mul func called")
            return Vector(scalar * dimension for dimension in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        print("rmul func called")
        return self * scalar

    def __matmul__(self, other):
        if isinstance(other, abc.Iterable):
            pairs = itertools.zip_longest(self, other, fillvalue=0)
            return sum(a * b for a, b in pairs)
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        return self * other

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(other) == len(self) and \
                all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

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
    print(v1 == +v1)
    print(v1 == [1, 2, 3])
    # 先正向调用Vector类的__eq__函数，然后再调用tuple的__eq__函数，结果都是NotImplemented
