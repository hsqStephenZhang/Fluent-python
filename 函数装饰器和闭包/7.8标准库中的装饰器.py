"""
标准库中提供了实用的装饰器，如lru_cache,singledispatch
"""
"""
lru_cache通过字典保存缓存信息，maxsize=128，自己设置应设置为2^i，
lru_cache可以极大地优化递归算法，也可以在从web获取信息的应用中发挥作用
"""
from functools import lru_cache

import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_msg = ", ".join(repr(arg) for arg in args)
        print("[%0.8fs] %s(%s) ->%r" % (elapsed, name, arg_msg, result))
        return result
    return clocked


@clock
@lru_cache(128)
def fabonaci(n):
    if n <= 1:
        return 1
    else:
        return fabonaci(n - 1) + fabonaci(n - 2)


if __name__ == '__main__':
    fabonaci(30)

