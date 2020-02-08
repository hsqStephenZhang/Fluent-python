"""
不要使用可变类型作为函数的参数的默认值
"""


class HauntedBus(object):
    def __init__(self, passengers=[]):  # python会提醒,不要使用mutable value
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        try:
            self.passengers.remove(name)
        except ValueError:
            print("student not in the bus")


class TwilightBus(object):
    def __init__(self, passengers=None):  # python会提醒,不要使用mutable value
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        try:
            self.passengers.remove(name)
        except ValueError:
            print("student not in the bus")


def show1():
    bus1 = HauntedBus(['Alice', 'Bill'])
    bus1.pick('charlie')
    bus1.drop("Alice")
    bus2 = HauntedBus()
    bus2.pick('Carrie')
    bus3 = HauntedBus()
    print(bus3.passengers)
    bus3.pick('Dave')
    print(bus2.passengers)
    print(bus2.passengers is bus3.passengers)
    """
    这里出现了灵异事件:bus3中的乘客出现在了bus2中，bus2中的乘客出现在了bus3中
    这是因为没有指定初始乘客的bus会共享一个乘客列表
    默认值是函数对象的属性，如果其是可变对象，则修改了之后对之后的所有的初始化默认值都会影响
    """


def show2():
    team = list("abcde")
    bus = TwilightBus(team)
    """
    这里TwilightBus中的passengers共享了team这个list，应当使用team的副本
    也就是将self.passengers=passengers 修改为 self.passengers=list(passengers)
    这样该类中操作的就是team的副本，而其中的元素又是不可变的类型，所以不会对原参数影响
    """
    bus.drop('a')
    bus.drop('b')
    print(team)


if __name__ == '__main__':
    # show1()
    show2()
