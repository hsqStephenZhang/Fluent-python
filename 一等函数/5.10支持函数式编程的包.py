"""
常用的包有operator,functools
"""

import operator
from functools import reduce,partial

# partial函数用来冻结参数
func1=operator.sub
func2=partial(func1,2) # 按顺序列出函数的参数，这里将第一个参数定为2
func3=partial(func1,1,4)
print(func2(3))
print(func3())

