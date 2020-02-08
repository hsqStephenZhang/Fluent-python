"""
什么是可散列类型？
原子不可变数据类型都是可散列类型，如str,bytes,数值类型，frozenset也是可散列的，因为
frozenset里面容纳的也都是可散列的类型对象，元组只有容纳的都是可散列类型的情况下才是
可散列的
"""
a = 1
b = "StephenZhang"
c = (a, b, [1, 2])
d=frozenset(range(10))
print(hash(a), hash(b),hash(d))
print(hash(c)) # list是不可散列的类型,因此会报错
