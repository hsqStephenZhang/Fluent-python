"""
python除了dict，还提供了几种变体，如collections 模块里面的OrderedDict,defaultdict
"""


import re

pattern=re.compile(r"\w+")
index={}
with open("3.3.data.txt", 'r') as fp:
    for line_no,line in enumerate(fp,1):
        for match in pattern.finditer(line):
            word=match.group()
            column_no=match.start()+1
            location=(line_no,column_no)
            # occurances=index.get(word,[])
            # occurances.append(location)
            # index[word]=occurances
            """ 
            效果和上面的三行是一样的，如果单词没有出现，则将单词和一个空的list放入
            映射，返回这个空list,等价于:
            if key not in my_dic:
                my_dic[key]=[]
            my_dic[key].append(value)
            """
            index.setdefault(word,[]).append(location)

for word in sorted(index,key=str.upper):
    print(word,index[word])