"""
可以通过装饰器来实现重复的功能
"""
registry = []


def register(func):
    registry.append(func)
    return func


@register
def strategy1(money):
    return money * 0.1


@register
def strategy2(money):
    if money < 500:
        return 0
    elif money < 1500:
        return money * 0.05
    else:
        return money * 15


if __name__ == '__main__':
    print(registry)

    """
    通过register装饰器实现了将销售策略加入到registry列表中,这样既十分方便，
    还十分易于扩展，也便于及时禁止使用某种策略
    """