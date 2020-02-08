"""
元组除了作为不可变的list，还可以用于没有字段名称的记录
"""

from collections import namedtuple
a = (1, 2)
print(a.index(1))  # 元组有index,count两个函数，分别输出元素第一次出现的位置和次数


# '*'作为运算符可以将可迭代对象拆分开
def add(a, b):
    return a + b


print(add(*a))
print(*a)

# 进一步研究*的拆分作用,*作为前缀可以出现在任意位置
a, b, *residual = range(5)
print(a, b, residual, type(residual))
a, *residual, b = range(2)
print(a, b, residual, type(residual))

# 具有名字的元组
# namedtuple所消耗的内存和元组是一样的，之前已经在第一章Python风格的纸牌里面使用了这个类
City = namedtuple('City', 'name country population')
a = City(name='Beijing', country='China', population=50000000)
print(a)
