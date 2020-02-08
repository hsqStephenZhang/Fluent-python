"""
增量赋值的结果取决于它们的第一个操作对象，两种增量赋值方法是 +=,*=
"""
"""
要注意一下几点:
1.元组内部不要存放可变对象
2.增量赋值不是一个原子操作，虽然抛出了异常，但是还是完成了操作
"""


def show1():
    l = [1, 2, 3]
    print(id(l))
    l *= 2
    print(id(l))
    l += [4, 5]
    print(id(l))  # 这几种操作均不会改变list的地址


def show2():
    l = (1, 2, [3, 4])
    print(id(l))
    try:
        l[2] += [5]
    except BaseException:
        print("Base Error!")  # 虽然发生了错误，但是仍然可以成功修改元组内部的list
        print(l, id(l))


def show3():
    a = 1
    print(id(a), end=" ")
    a += 1  # 会开辟一个新的存储空间来存放a+1之后的值，然后给这个对象打上标签a
    print(id(a))
    b = "hhh"
    print(id(b), end=" ")
    # 在字符串后面连接字符串很常见，因此，一般的字符串都会预留一定的空间，不用复制到更大的空间去
    b += "lll"
    print(id(b))


if __name__ == '__main__':
    # show1()
    # show2()
    show3()
