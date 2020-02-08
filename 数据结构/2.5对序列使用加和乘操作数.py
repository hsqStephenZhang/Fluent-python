"""
常见的是对list使用+和*这两种操作，但是，也需要考虑到一些潜在的问题
"""


def show():
    l = [[1], 2, 3]
    a = l * 5
    print(a)
    l[0][0] = 10  # 因为这里保存的是对[1]的引用，所以修改了[1]内部的元素的值，所有的引用都会修改
    print(a)


def show2():
    a = []
    for i in range(3):
        l = [[1], 2, 3]  # 每次都创建了一个新的list，这样就不会存在重复引用的问题
        a.append(l)
    print(a)
    a[0][0] = 10
    print(a)


if __name__ == '__main__':
    # show()
    show2()
