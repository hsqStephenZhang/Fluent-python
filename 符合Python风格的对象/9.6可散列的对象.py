"""
对于一个普通的object来说，一般是不可散列的，要是想将其放入set中，还需要定义__hash__方法
同时还需要实现__eq__方法
"""

class Show(object):
    def __init__(self,x,y):
        self.__x=float(x)
        self.__y=float(y)

    @property
    def x(self): # 实例的散列值绝对不应该变化，所以需要使用只读属性
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x)^hash(self.y)&(hash(self.x)+hash(self.y))

    def __eq__(self, other):
        return tuple(self)==tuple(other)

    def __iter__(self):
        return (i for i in (self.x,self.y))

if __name__ == '__main__':
    a=Show(1,2)
    b=Show(2,3)
    myset={a,b} # 必须要实现__hash__方法才可以加入到set和dict等容器中
    print(myset)
