"""
生成器函数可以用来代替SentenceIterator类的作用

生成器函数yield是生成器工厂
"""

import re
import reprlib
pattern = re.compile(r"\w+")


class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = re.findall(pattern, text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return  # 这个return不是必须的


def show1():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    s = Sentence("I love China.May god bless all of us")
    print(type(iter(s)))  # 内置的generator
    print(type(show1),type(show1()))
