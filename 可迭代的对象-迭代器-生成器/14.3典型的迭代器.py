"""
可迭代的对象的__iter__方法每次都会实例化一个新的迭代器，不能实现__next__方法
Iterator要实现__next__方法，还要实现__iter__方法，返回自身

迭代器的好处有:
访问一个对象而无需暴露其内部的表示
为一个对象提供多种遍历方式
为不同的对象提供相似的遍历方法
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
        return SentenceIterator(self.words)



class SentenceIterator(object):

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    s = Sentence("The time has come,said Walrus")
    print(type(iter(s)))
    for i in s:
        print(i,end=" ")


