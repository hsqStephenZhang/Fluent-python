"""
模拟校车在旅途中上车和下车
"""
import copy


class Bus(object):
    def __init__(self, passenger=None):
        if passenger is None:
            self.passenger = []
        else:
            self.passenger = list(passenger)

    def pick(self, name):
        self.passenger.append(name)

    def drop(self, name):
        try:
            self.passenger.remove(name)
        except ValueError:
            print("Student not on the bus")


if __name__ == '__main__':
    bus1 = Bus(['Alice', 'Bob', 'Mary', 'Red'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))
    bus1.drop('Bob')
    bus3.drop('Black')
    print(bus1.passenger)
    print(bus2.passenger)  # bus1中的Bob被drop了，但是list是可变对象，所以bus2也随之改变
    print(bus3.passenger)
