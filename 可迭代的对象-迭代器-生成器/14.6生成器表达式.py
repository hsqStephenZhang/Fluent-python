"""
生成器表达式只是一个语法糖
完全可以用生成器函数替代，只不过实现起来有时候更方便
对于一些简单的推导式完全可以采用生成器表达式
"""


def show1():
    a = (i for i in range(5))  # 类似list推导式
    print(type(a))
    for elem in a:
        print(elem, end=" ")


if __name__ == '__main__':
    show1()
