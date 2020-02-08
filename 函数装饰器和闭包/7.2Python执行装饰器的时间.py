"""
Python何时执行装饰器？
对于装饰器，其执行的时间就是刚刚被定义之后,立即执行
"""

registry = []


def register(func):
    print("running register {}".format(func))
    registry.append(func)
    return func


@register
def add(a, b):
    return a + b


@register
def mul(a, b):
    return a * b


if __name__ == '__main__':
    print("running main")  # 这句话是在装饰器执行之后再输出的
    add(1, 2)
    mul(1, 2)
