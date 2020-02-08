"""
Python中的垃圾回收的主要方法是引用计数，当一个对象的引用计数被清零时，其就被销毁了
自己写程序很少需要重载__del__方法，因为其很难完全用对
"""
import weakref

def bye():
    print("Gone with the wind...")

if __name__ == '__main__':
    s1={1,2,3}
    s2=s1
    ender=weakref.finalize(s1,bye)
    del s1
    print(ender.alive)
    s2={1,2}
    # 此时，已经没有了对s1原来所指的对象{1,2,3}的引用了，只剩下finalize函数的弱引用，但是
    # 并不妨碍其引用计数清零
    print(ender.alive)
