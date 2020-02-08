"""
因为继承了MutableSequence，所以必须要实现__delitem__,insert,__setitem__等抽象方法
"""


import collections
import random


Card = collections.namedtuple('Card', ['number', 'suit'])


class Deck(collections.abc.MutableSequence):
    numbers = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades clubs diamonds hearts".split(" ")

    def __init__(self):
        self._cards = [Card(number, suit) for number in self.numbers
                       for suit in self.suits]

    def shuffle(self):
        random.shuffle(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, index, value):
        self._cards[index] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, index, val):
        self._cards.insert(index, val)


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    a = [deck[i * 13:i * 13 + 13] for i in range(4)]
    for item in a:
        print(item)
    print(Card(number='10', suit='clubs') in deck)  # 数据是可迭代的
    print(dir(collections.abc.MutableSequence))  # 并不是每一个方法都是抽象的
