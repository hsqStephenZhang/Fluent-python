"""
多重继承有优点也有缺点
很明显的缺点就是通过多重继承增加了代码的复杂度和框架的脆弱性

多重继承的时候要注意一下几点：
1.接口继承和(方法)实现继承区分开
2.使用抽象基类显示表示接口
3.通过混入重用代码(Mixin 表示某个类只是为了其他的类打包方法，从而避免重用，
而不是为了具体化，这样的混入类绝对不可以实例化)
4.在名称中明确指明混入
5.不要子类化多个具体的类
6.优先使用对象组合，而不是类继承
"""

""" 
多重继承本身没有问题，但是绝对不是灵丹妙药，具体应用的时候再说
"""


