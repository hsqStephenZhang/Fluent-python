"""
使用bisect要求的一个序列是已经排好序的，numpy中也有二分搜索的函数，但是对于一般的
序列(非numpy数组)来说，使用bisect包要快很多
"""

import bisect
import sys
import random

random.seed(7)


def show1():
    """
    如果查找的值已经存在，那么
    bisect.bisect_left 找的是该值之前的位置，bisect.bisect_left找的是该值之后的位置
    """
    a = sorted([1,3,4,4,7,8,9])
    print(a)
    c = bisect.bisect_left(a, 4)  # 查找应该插入的位置,而不进行实际的插入
    d = bisect.bisect_right(a, 4)
    print(c, d)
    bisect.insort_left(a,1)
    print(a)

if __name__ == '__main__':
    show1()
