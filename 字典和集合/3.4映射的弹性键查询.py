"""import re
from collections import defaultdict

pattern=re.compile(r"\w+")
index=defaultdict(list)  # 通过defaultdict直接设置键不存在时候的创造默认值的方法
with open("3.3.data.txt", 'r') as fp:
    for line_no,line in enumerate(fp,1):
        for match in pattern.finditer(line):
            word=match.group()
            column_no=match.start()+1
            location=(line_no,column_no)
            index[word].append(location)

for word in sorted(index,key=str.upper):
    print(word,index[word])
"""

""" 
有的时候，需要实现键全部为str类型的字典，当用户输入的是数字的时候，需要判断其对应的
字符是否在keys中，不能直接抛出keyerror
"""
class Strdict(dict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError("{} doesn't exist".format(key))
        else : return self[str(key)]

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()

    def get(self,key,default=None):
        try:
            return self[key]
        except  KeyError:
            return default


if __name__ == '__main__':
    my_strdict=Strdict()
    my_strdict['1']=1
    print(my_strdict[1])
    print(3 in my_strdict.keys())
    print(my_strdict.get(5))
    print(my_strdict[2])

