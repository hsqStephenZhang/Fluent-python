"""
对象之间的比较
"""


def show1():
    dic1 = {1: 'a', 2: 'b'}
    dic2 = dic1
    dic2[3] = 'c'
    dic3 = {1: 'a', 2: 'b', 3: 'c'}
    print(dic1)
    print(dic1 is dic2, id(dic1) == id(dic2))
    print(dic3 == dic1, dic3 is dic1)
    """
    dic3和dic1的比较结果虽然是相等的，但是它们不是同一个对象
    id() 和 is 的作用是一样的，都是比较对象的标识，这个标识从对象被创建就不会改变
    """


def show2():
    x = None
    print(x is None, x is not None)
    b = 1
    print(b is 1)
    """
    is运算符比==快，因为其不能重载，Python不会寻找特殊方法
    但是,平时用的比较多的是==，因为大部分情况比较的是两者是不是相等，而不是比较指向的
    是不是同一个对象
    但是，在对int，None这种单例值作比较的时候，用is更好
    """


def show3():
    t1 = (1, 2, [3, 4])
    t2 = (1, 2, [3, 4])
    print(t1 == t2, t1 is t2)
    t1[-1].append(5)
    print(t1, t1 == t2)
    """
    元组的不可变性指的是元组包括的元素是不可变的，但是元组内的元素指代的对象有的是
    可变的，如list
    这也印证了元组有的时候是可散列的，有的时候是不可散列的
    """


if __name__ == '__main__':
    # show1()
    # show2()
    show3()
