"""
除了show1中的递归文件系统之外，itertools还提供了几大类生成器
1.过滤;2.映射;3.无中生有
"""

import os
import itertools


def show1():  # 递归搜索文件系统
    for root, dirs, file in os.walk("E:/DESKTOP/GitHub"):
        if dirs:
            print("root:{},dirs:{}".format(root, dirs))
        else:
            print("files:{}".format(file))


def show2():
    a = [i for i in range(2)]
    b = [j for j in range(4)]
    for a1, b1 in itertools.zip_longest(a, b, fillvalue=-1):  # 以较长的可迭代对象为准
        print(a1, ":", b1, end=",")
    print("\n", end="")
    try:
        for a1, b1 in zip(a, b):  # 只要有一个可迭代对象到头了,就停止了
            print("{}:{}".format(a1, b1), end=" ")
    except BaseException:
        print("two iter object's length don't match")


def show3():
    a = [1, 2, 3]
    b = [4, 5, 6]
    for i in itertools.chain(a, b):
        print(i, end=" ")


def show4():  # 生成笛卡尔积
    a = [1, 2, 3]
    b = list("abc")
    for elem in itertools.product(a, b, repeat=2):
        print(elem, end=" ")


def show5():
    nums = ['a', 'C', 'c', 'B', 'B', '1']
    myiter = itertools.groupby(nums, key=lambda x: (x.isdigit()))
    for key, value in myiter:
        print(key, list(value), sep=":", end=" ")


if __name__ == '__main__':
    # show1()
    # show2()
    # show3()
    # show4()
    show5()
