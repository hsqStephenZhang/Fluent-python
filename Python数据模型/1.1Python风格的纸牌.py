import collections
import random

"""
Python数据模型的好处:
1.不用记住各种标准操作的名称
2.不用重新发明轮子，只需要利用现有的常用的库函数即可
"""


Card = collections.namedtuple('Card', ['number', 'suit'])


class Deck(object):
    numbers = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades clubs diamonds hearts".split(" ")

    def __init__(self):
        self._cards = [Card(number, suit) for number in self.numbers
                       for suit in self.suits]

    def shuffle(self):
        """
        一般来说在类的外面是无法洗牌的，
        只有在类里面定义函数直接对_card操作才可以洗牌
        """
        random.shuffle(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        """
        使用该方法可以将self.card变成可以迭代的对象
        """
        return self._cards[position]


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle() # 无法直接用random.shuffle(deck)实现洗牌
    print(len(deck))  # 自己重新写了__len__()函数，否则无法直接用len()求出其长度
    a = [deck[i * 13:i * 13 + 13] for i in range(4)]
    for item in a:
        print(item)
    print(Card(number='10', suit='clubs') in deck)  # 数据是可迭代的
