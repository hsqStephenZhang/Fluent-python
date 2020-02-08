"""
python的内置的format()函数和str.format()方法将每个类型的格式化输出的方式委托给了相应的
.__format__(format_spec)方法
"""

"""
常用的format格式有:
"""

from datetime import datetime

def show():
    print("{:0f} {:.2f} {:.4f}".format(1, 1, 1))
    print("{:0>2d} {:0>4d} {:0>8d}".format(1, 1, 1))  # 从左边补零
    print("{:0<2d} {:0<4d} {:0<8d}".format(1, 1, 1))  # 从右边补零
    print("{:x<2d} {:x<4d} {:x<8d}".format(1, 1, 1))  # 从右边补x
    print("{:,}".format(10000000))  # 以逗号的形式分隔
    print("{:.2%} {:.4%}".format(0.5, 0.5))  # 输出百分比的形式
    print("{:.2e} {:.4e}".format(1000, 1000))  # 输出指数的形式，数字表示保留的位数
    print("{:.<5}".format(10))  # 左对齐，这里制定了用'.'填充，如果没有指定，则用空格填充
    print("{:.>5}".format(10))  # 右对齐
    print("{:.^5}".format(10))  # 居中对齐
    print("{:%H:%M:%S}".format(datetime.now()))  # 具体的(小时:分钟:秒)的时间
    print("It's now {:%I:%M %p}".format(datetime.now()))  # 小时:分钟 上午/下午 的时间
    print("{:b} {:d} {:o} {:x}".format(11, 11, 11, 11))  # 各种进位制度的显示


if __name__ == '__main__':
    show()
