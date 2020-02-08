"""
Python中的参数传递是共享传参，传入的是实参中各个引用的副本
"""


def func(a, b):
    """
    因为传入的是各个引用的副本，而如果a,b是不可变类型，则不会影响实参
    如果a,b是list类型的话，对a和b的改变就会反映到实参上面
    """
    a += b
    print(a, id(a))  # 当a为list类型的时候，+=操作不会改变a的id，a为其它可变类型的时候，id会改变
    return a + b


if __name__ == '__main__':
    x = [1, 2]
    y = [3, 4]
    print(x, id(x))
    func(x, y)
    print(x, id(x))
