"""
因为这是一个向量，所以最好要实现v.x,v.y,v.z等直接取出向量的分量的操作
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
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            raise TypeError("Wrong input")

    def __setattr__(self, name, value):
        """
        现在问题是向量是通过传入一个list来创建的，而对于vector来说，有x,y,z等分量
        假如直接令v.x=1，这样是直接创建了一个新的属性，而对self._components没有影响
        也就是发生了歧义
        """
        shortcutname = list("xyz")
        cls = type(self)
        if len(name) == 1:
            if name in shortcutname:
                error = "readonly input"
            elif name.isupper():
                error = "cannot set attribute from 'A' to 'Z' "
            else:
                error = ""
            if error:
                raise AttributeError(error)
        super(Vector).__setattr__(name,value)


if __name__ == '__main__':
    v1=Vector([1,2,3])
    print(v1)
