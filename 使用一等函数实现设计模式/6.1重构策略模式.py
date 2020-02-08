"""
一个网店制定了下述折扣规则:
1.1000积分以上的顾客，享受5%的优惠
2.同一个订单中，单个商品的数量达到20个及以上，享受10%优惠
3.订单中不同商品的种类达到10个及以上，享受7%优惠

“策略”模式涉及以下内容:
1、上下文：把一些计算委托给不同的组件进行，自己则提供服务
2、策略：实现不同的算法的不同的接口
3、具体策略：策略的具体子类

"""
from collections import namedtuple
from abc import abstractmethod, ABC

Customer = namedtuple("Customer", "name fidelity")


class Lineitem(object):
    def __init__(self, product, quantity, price):
        self.product = product  # 产品名称
        self.quantity = quantity  # 数量
        self.price = price  # 价格

    def total(self):  # 总价
        return self.price * self.quantity


class Order(object):
    def __init__(self, customer, cart, promotion):
        self.customer = customer  # 一个具名元组
        self.cart = list(cart)  # 一个可迭代对象转换而来的list
        self.promotion = promotion  # 促销策略

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):  # 应付的钱=总价-促销减去的钱
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.__total - discount

    def __repr__(self):
        fmt = "< Order total: {:.2f} due:{:.2f} >"
        return fmt.format(self.total(), self.due())


class Promotion(object):
    @abstractmethod
    def discount(self, order):
        """抽象方法,提供接口"""


class FidelityPromo(Promotion):
    """ 积分多于1000的客户提供5%的优惠"""

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity > 1000 else 0


class AmountPromo(Promotion):
    """购买单件物品的数量多于20的客户提供10%的优惠"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity > 20:
                discount += item.total()
        return discount


class KindsPromo(Promotion):
    """购买商品的种类多于10的客户提供7%的优惠"""

    def discount(self, order):
        kinds = {item.product for item in order.cart}
        if len(kinds) > 10:
            return sum(item.total for item in order.cart) * 0.07
        else:
            return 0


if __name__ == '__main__':
    joe = Customer("john", 0)
    ann = Customer("Ann", 1100)
    cart = [
        Lineitem(
            'banana', 4, .5), Lineitem(
            'apple', 10, 1.5), Lineitem(
                'watermelon', 4, 1.2)]
    order1 = Order(joe, cart, FidelityPromo())
    order2 = Order(ann, cart, FidelityPromo())
    print(order1.due)
    print(order2.due)
