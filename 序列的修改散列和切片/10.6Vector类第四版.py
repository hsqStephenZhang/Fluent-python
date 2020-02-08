"""
实现hash方法，也就是要在原来Vector2D的基础上写出具有多个分量的__hash__函数
这时候就需要使用functools里面的reduce函数了，而且可以直接使用operator包里面的二元运算符
operator包包含了所有的二元运算符
"""

from functools import reduce
import operator


def myhash(nums1):
    nums1 = map(hash, nums1)
    return reduce(operator.xor, nums1)


def myeq(nums1, nums2):
    return len(nums1) == len(nums2) and all(
        item1 == item2 for item1, item2 in zip(nums1, nums2))
    # map 和 zip 都是惰性计算，所以效率比较高
