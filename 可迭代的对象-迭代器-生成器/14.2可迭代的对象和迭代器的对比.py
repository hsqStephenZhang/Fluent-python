"""
Python从可迭代的对象中获取迭代器

检查一个对象是否是迭代器的最好的方法就是isinstance(a,abc.Iterator)
因为其实现了__subclasshook__的方法，可以判断该实例的类的父类中是否有__next__,__iter__方法
"""

from collections import abc

def show1():
    s="abcdef"
    it=iter(s)
    while True:
        try:
            print(next(it),end=" ")
        except StopIteration:  # StopIteration表明迭代到头了 
            del it
            break


if __name__ == '__main__':
    show1()
    print(dir(abc.Iterator))
