"""
除了__slot__属性中添加的属性以外，不能够再给类的实例添加更多的属性，除非将__dict__重新添加到
__slot__中，但是那样完全违背了__slot__的使用的初衷
__slot__是不支持继承的，所以每一个子类中都必须要重新定义
如果是需要弱引用的对象，需要在__slot__中添加__weakref__属性
"""


class Show(object):
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    a = Show(1, 2)
    print(a.__slots__)
