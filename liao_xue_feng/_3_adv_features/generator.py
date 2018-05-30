# -*- coding: utf-8 -*-

# a simple generator
print('a simple generator')
g1 = (x * x for x in range(1, 11))
for n in g1:
    print(n)

# another form of g1
print('another form of g1')


def g2(start, stop):
    while start < stop:
        yield start * start
        start = start + 1


for n in g2(1, 11):
    print(n)

# Fibonacci generator
print('Fibonacci generator')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for x in fib(10):
    print(x)

fib_list = list(fib(10))  # create a list using generator
print(fib_list)

# Yang Hui Triangle
print('Yang Hui Triangle')


def yh_triangle(max):
    n = 1
    lv_current = [1]
    while n <= max:
        if n == 1:
            yield lv_current
        elif n >= 2:
            lv_next = [0 for x in range(n)]  # generate a list of zero
            for idx in range(n):
                if idx == 0 or idx == n - 1:
                    lv_next[idx] = 1
                else:
                    lv_next[idx] = lv_current[idx] + lv_current[idx - 1]
            lv_current = lv_next
            yield lv_current
        else:
            yield []
        n = n + 1


for lv in yh_triangle(10):
    print(lv)
