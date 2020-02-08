"""
对一个对象复制的时候，要注意这个是可变的还是不可变的
"""


def show1():
    a = [1, 2, 3, 4]
    b = a[:]
    print(a is b, id(a), id(b))
    a.append(5)
    a[0] = 10
    a.pop(1)
    print(b)
    # 因为a的所有的元素都是不可变的，所以这里浅复制达到了深复制的效果,还可以节省内存


def show2():
    a = [[1, 2, 3], (4, 5)]
    b = a[:]
    a[0].append(10)
    a[1] += (6, 7)  # 对于一个元组来说，+=运算符创建了一个新的元组
    print(a)
    print(b)



if __name__ == '__main__':
    show1()
    # show2()
