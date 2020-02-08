"""
本节讨论Python的参数处理机制
通过*传入可变长度的元组,通过**传入字典
"""


def show(a, *args, **kwargs):
    print(a)
    for i in args:
        print(i,end=" ")
    print("\n",end="")
    for key, value in kwargs.items():
        print("{}:{}".format(key, value),end=" ")


if __name__ == '__main__':
    show(1, 2, 3, 4, 5, **{"1": 1, "2": 2, "3": 3})

    """
    Tips:字典的keys必须是strings,且传入字典的话要在前面加上**标签，否则如果有*args
    的话，会被整个当做一个可变长度的args中的一个参数传入
    """
