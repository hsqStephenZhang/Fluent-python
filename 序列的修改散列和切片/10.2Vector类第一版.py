"""
构造一个多维的向量类，其接受多个维度的参数的最好的方法就是接受一个可迭代的对象
使用array而不是list可以节省存储空间
"""


from array import array
import reprlib
import math


class Vector(object):
    typecode = 'd'

    def __init__(self, components):
        self._components=array(self.typecode,components)

    def __iter__(self):  # 返回一个迭代器
        return iter(self._components)

    def __repr__(self):
        components=reprlib.repr(self._components)
        components=components[components.find('['):-1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __hash__(self):
        result=0
        for item in self._components:
            result=result^hash(item) # 简单的异或还不完善
        return result

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self._components)) # 欧氏距离的函数

    def __bool__(self):
        return bool(abs(self))

    """ 
    缺少了一个方法，就是从Vector2D的bytes二进制码重构该类的实例
    """


if __name__ == '__main__':
    v1 = Vector([3,4,5,6,7,8,9,10])
    # print(abs(v1))
    # print(bytes(v1))
    print(repr(v1))
    v2=Vector([1,2,3])
    print(v1==v2)
    a={v1,v2}
    print(a)