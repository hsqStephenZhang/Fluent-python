"""
实现一个简单的输出函数的运行时间等信息的装饰器
"""

from functools import wraps
import time


def clock(func):
    @wraps(func)  # 通过这个装饰器，保留了原函数的__name__和__doc__信息
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
def fabonaci(n):
    """this is fabonaci function"""

    if n <= 1:
        return 1
    else:
        return fabonaci(n - 1) + fabonaci(n - 2)


if __name__ == '__main__':
    print(fabonaci.__name__)
    print(fabonaci.__doc__)
