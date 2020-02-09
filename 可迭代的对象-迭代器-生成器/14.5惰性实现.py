"""
上一节中放入re.findall返回的是一个list，也就不是惰性实现，为了使得这个变得懒惰
可以使用re.finditer()函数，返回的将是一个生成器

惰性实现的好处就是可以节省内存，而且可以避免无用的处理
"""

import re
import reprlib
pattern = re.compile(r"\w+")


class Sentence(object):

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        for word in re.finditer(pattern,self.text):
            yield word.group()
        return  # 这个return不是必须的




if __name__ == '__main__':
    s = Sentence("I love China.May god bless all of us")
    g=iter(s)
    for i in g:
        print(i,end=" | ")
