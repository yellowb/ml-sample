# -*- coding: utf-8 -*-


# Not tail optimization recursive
def fact_not_tail(n):
    if n == 1:
        return 1
    else:
        return n * fact_not_tail(n - 1)


print(fact_not_tail(10))


# Tail optimization recursive
def fact_tail(n, summary):
    if n > 1:
        return fact_tail(n - 1, summary * n)
    else:
        return summary


def fact_tail_wrapper(n):
    return fact_tail(n, 1)


print(fact_tail(10, 1))
