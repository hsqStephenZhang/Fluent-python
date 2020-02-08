"""
list.sort会就地对list进行排序，返回值为None，这是为了表明该操作对原来的对象进行了修改
但是不会返回新的对象
与之相反，sorted函数会返回一个新的排序之后的list
"""
"""
Python中的内置的排序算法叫Timbot,它根据序列的特点交替使用快速和归并排序，以达到最高的效率
"""

import random
random.seed(7)


def show1():
    l = [random.randrange(0, 14) for i in range(8)]
    print(l)
    l.sort(key=int, reverse=True)
    print(l)


def show2():
    strings = list("HSQzcLJhui315792")
    print(strings)
    strings.sort()  # 区分大小写
    print(strings)
    strings.sort(key=str.upper)  # 不区分大小写
    print(strings)
    strings.sort(
        key=lambda x: (
            x.isdigit(),
            x.isdigit() and int(x) %2 == 1,
            x.isupper(),
            x))
    print(strings)
    # 使用Lambda表达式作为key的话,其排序的顺序就是从前往后，满足该条件的往后排，不满足条件的往前排


if __name__ == '__main__':
    # show1()
    show2()
    from frozenlist import FrozenList
    a=FrozenList([1,2])
    a.freeze()
    print(a)
