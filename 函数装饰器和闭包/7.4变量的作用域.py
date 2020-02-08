"""
函数内部的局部变量的作用域十分有讲究
可以通过字节码编译结果了解情况
"""


def show1():
    b = 6

    def func(a):
        nonlocal b
        print(a, end=" ")
        print(b, end=" ")
        b += 1
        print(b)

    func(3)
    print(b)
    """
    这样是可以输出a的，但是b会报错，这是因为在函数内将b赋值，解释为了局部变量
    和外部的b就没有关系了
    """


def show2():
    b = 6

    def func(a):
        print(a, end=" ")
        print(b)
    func(3)
    """
    这里是可以正常输出的，因为对于func里面的b来说，其是全局变量
    """


b = 6


def func(a):
    global b
    print(a, end=" ")
    print(b, end=" ")
    b = 9
    print(b)


# show2()
func(3)
print(b)
# show1()
