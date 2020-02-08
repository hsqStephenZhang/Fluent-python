import collections

class Strdict(collections.UserDict):
    """
    使用UserDict来进行拓展更加友好，其有一个data属性，是用来存储数据的地方
    实现__setitem__的时候就可以避免不必要的递归
    """

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError("{} doesn't exist".format(key))
        return self[str(key)]

    def __setitem__(self, key, value):
        self.data[str(key)] = value

    def __contains__(self, item):
        return item in self.data

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


if __name__ == '__main__':
    my_strdict = Strdict()
    my_strdict[1] = 1
    my_strdict[2] = 2
    my_strdict[3] = 3
    print(my_strdict.items())
    print(4 in my_strdict)
