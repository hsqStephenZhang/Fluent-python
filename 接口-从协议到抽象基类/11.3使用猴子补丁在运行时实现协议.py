import collections
import random


Card = collections.namedtuple('Card', ['number', 'suit'])


class Deck(object):
    numbers = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades clubs diamonds hearts".split(" ")

    def __init__(self):
        self._cards = [Card(number, suit) for number in self.numbers
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        """
        使用该方法可以将self.card变成可以迭代的对象
        """
        return self._cards[position]

    def set_card(self, pos, val):
        self._cards[pos] = val


def show1():
    deck1 = Deck()
    random.shuffle(deck1)
    # 这里是无法实现直接的shuffle一个Deck实例


def show2():
    deck2 = Deck()
    Deck.__setitem__ = deck2.set_card  # 通过猴子补丁实现了__setitem__方法
    random.shuffle(deck2)
    print(deck2[:5])


if __name__ == '__main__':
    # show1()
    show2()
    print(dir(Deck))  # 在show2中打了一个猴子补丁，但是这个补丁是暂时的
