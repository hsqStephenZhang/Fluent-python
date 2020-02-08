"""
collections.abc 和 numbers提供了大多数的抽象基类
"""

from collections import abc
import numbers


""" 
numbers分为:
Number,Complex,Real,Rational,Integral
"""

print(isinstance(1.4,numbers.Real))
print(isinstance(1.4,numbers.Integral))
print()
