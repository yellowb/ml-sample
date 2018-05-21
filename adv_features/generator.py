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


