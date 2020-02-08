"""
通过singledispatch装饰器实现对不同的类型的对象的不同的输出，而不需要判断type(obj)
到底是什么，而且支持模块化扩展
各个专门的函数通过@<<base function>>.register(<<type>>)修饰
尽量实现抽象基类，如numbers.Intergral这种抽象类型的对象，这样比int类型更容易扩展
"""


from functools import singledispatch
import numbers


@singledispatch
def show(obj):
    return "{}".format(obj)


@show.register(str)
def show_text(text):
    content = text.split(" ")
    return "<pre>{}</pre>".format(content)


@show.register(numbers.Integral)
def show_number(number):
    return "number:{}".format(number)


if __name__ == '__main__':
    print(show(10))
    print(show("hhh succeed"))
