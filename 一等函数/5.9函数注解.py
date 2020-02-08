"""
输出函数的注释信息，包括各个参数以及返回值,这里不是引号里面的内容，而是
函数的第一行的声明信息
"""


def add(a: int, b: int) -> int:
    """this is my kingdom
    """
    return a + b


print(add.__annotations__) # 对各个参数以及返回值的注释信息
print(add.__name__)
print(add.__call__)
