# -*- coding: utf-8 -*-

# list
L = [1, 2, 3, 4, 5]
for item in L:
    print(item)

# tuple
T = tuple(L)
for item in T:
    print(item)

# dict
D = {
    'a': 1,
    'b': 2,
    'c': 3
}
for key in D:
    print(key, ' -> ', D[key])
# another way to iterate dict
for key, value in D.items():
    print(key, ' -> ', value)

# generator
for i in range(10):
    print(i)

# how to check an object can be iterated
from collections import Iterable
print(isinstance(T, Iterable))
print(isinstance(D, Iterable))
print(isinstance(range(10), Iterable))
print(isinstance('abc', Iterable))


# iterate list with index and element
for idx, el in enumerate(['A', 'B', 'C']):
    print(idx, ' -> ', el)

