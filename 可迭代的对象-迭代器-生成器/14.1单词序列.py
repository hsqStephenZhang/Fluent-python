"""
任何Python序列都可迭代的原因是，它们都实现了__getitem__方法，标准的序列也都实现了__iter__方法
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

    def __repr__(self):
        return "Sentence({})".format(reprlib.repr(self.text))


if __name__ == '__main__':
    s = Sentence("The time has come,said walrus")
    print(s[1], s)
    print(s.text, s.words)
    a = 1
    try:  # 使用iter()的方法先检查能否迭代，因为假如有__getitem__方法的话也是可以迭代的，而不是直接用isinstance(s,abc.Iterable)
        iter(s)
        print("iterable")
    except TypeError:
        raise TypeError("cannot be itered")
