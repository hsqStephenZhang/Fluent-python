"""
可以将函数作为函数的参数的函数就是高阶函数
如map,reduce,filter,all,any
但是map,reduce,filter现在已经被list推导式很好地替代了
"""
import operator
from functools import reduce

a=[1,2,3,0]
print(all(a))
print(any(a))
print(reduce(operator.add,a))
print(list(map(lambda x:x^2,a)))
print(list(filter(lambda x:x>2,a)))

