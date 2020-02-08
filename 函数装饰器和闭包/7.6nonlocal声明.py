"""
nonlocal函数可以将变量声明为非局部变量(外部变量，而非全局变量)，
这样修改之后函数之外的该变量也被修改了
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


def show2():
    b = 6

    def func(a):
        global b # 会报错，因为这里的b不是全局变量，而是外层函数的局部变量
        print(a, end=" ")
        print(b, end=" ")
        b += 1
        print(b)

    func(3)
    print(b)


show1()
show2()
