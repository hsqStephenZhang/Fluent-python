from unicodedata import normalize

s1="cafe\u0301"
s2="café"  # é 和 e\u0301 是标准等价物
print(s1,s2,sep="  ")
print(s1==s2)

""" 
实际使用的时候应该使用normalize函数清洗字符串
有NFC和NFD两种方式来规范化，一种是使用最少的码位来表示，另一种是把组合字符拆解为
单独的组合字符和基字符
有一些意外情况，到时候注意即可
"""
print(len(s1))
s1=normalize("NFC",s1)
print(len(s1))


