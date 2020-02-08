from collections import namedtuple

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
            discount = self.promotion(self)
        return self.__total - discount

    def __repr__(self):
        fmt = "< Order total: {:.2f} due:{:.2f} >"
        return fmt.format(self.total(), self.due())


def FidelityPromo(order):
    """ 积分多于1000的客户提供5%的优惠"""

    return order.total() * 0.05 if order.customer.fidelity > 1000 else 0


def AmountPromo(order):
    """购买单件物品的数量多于20的客户提供10%的优惠"""

    discount = 0
    for item in order.cart:
        if item.quantity > 20:
            discount += item.total()
    return discount


def KindsPromo(order):
    """购买商品的种类多于10的客户提供7%的优惠"""

    kinds = {item.product for item in order.cart}
    if len(kinds) > 10:
        return sum(item.total for item in order.cart) * 0.07
    else:
        return 0

def best_promo(order):
    promos=[FidelityPromo,AmountPromo,KindsPromo]
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer("john", 0)
    ann = Customer("Ann", 1100)
    cart = [
        Lineitem(
            'banana', 4, .5), Lineitem(
            'apple', 10, 2.5), Lineitem(
                'watermelon', 4, 1.6)]
    order1 = Order(joe, cart, FidelityPromo)
    order2 = Order(ann, cart, FidelityPromo)
    print(order1.due)
    print(order2.due)
