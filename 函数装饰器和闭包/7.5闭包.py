"""
只有涉及嵌套函数的时候才会出现闭包的问题
闭包是一种函数，保留定义函数的时候的自由变量的绑定，再次调用的时候
仍然可以使用那些绑定
"""


def make_average():
    series=[]

    def average(number):
        series.append(number)
        print(sum(series)/len(series))
        return sum(series)/len(series)
    return average

if __name__ == '__main__':
    func=make_average()
    func(1)
    func(2)
    func(3)

