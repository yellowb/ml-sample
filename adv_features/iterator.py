# -*- coding: utf-8 -*-

from collections import Iterable
from collections import Iterator

print(isinstance(range(10), Iterable))
print(isinstance(range(10), Iterator))  # False

print(isinstance((x * x for x in range(10)), Iterable))  # True
print(isinstance((x * x for x in range(10)), Iterator))  # True

# Convert list to iterator
itor = iter([1, 2, 3])
print(isinstance(itor, Iterator))  # True
for n in itor:
    print(n)


