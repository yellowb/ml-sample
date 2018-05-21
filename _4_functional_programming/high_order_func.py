# -*- coding: utf-8 -*-
# High order function sample.


def square(x):
    return x * x


def high_order(x, y, func):
    return func(x) + func(y)


print(high_order(3, 4, square))

