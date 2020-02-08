"""
只需要实现__call__方法，任何的Python对象都可以表现得像函数
"""
import random


class BingoCage(object):
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except BaseException:
            raise LookupError("Pick from an empty cage")

    def __call__(self): # 为self.pick() 方法创建了一个快捷方式
        return self.pick()


if __name__ == '__main__':
    bingo=BingoCage(range(10))
    print(bingo())
    print(bingo.pick())
    print(len(bingo._items))
