"""
集合在Python中算是比较年轻的数据类型，在集合出现之前，都是将字典当做集合来用
集合常常用于去重，构造方法也是要求元素是可散列的
"""

a = {}  # 创建的是空字典
b = set()
print(type(a), type(b))

from dis import dis
dis('{1}')
dis('set([1])')
