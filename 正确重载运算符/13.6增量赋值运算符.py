"""
对于不可变对象来说，一定不可以实现就地修改的特殊方法，比如这里的Vector类


"""


def show1():
    print(hasattr(list, "__iadd__"), end=" ")
    print(hasattr(tuple, "__iadd__"), end=" ")
    print(hasattr(dict, "__iadd__"), end=" ")
    print(hasattr(int, "__iadd__"))


def show2():
    a = 1
    print(id(a),end=" ")
    a += 1
    print(id(a))
    t = (1, 2)
    print(id(t),end=" ")
    t += (3, 2)
    print(id(t))
    l = [1, 2]
    print(id(l),end=" ")
    l += [3, 2]
    print(id(l))   # 只有list的iadd方法不会改变原来的对象


if __name__ == '__main__':
    show1()
    show2()
