# -*- coding: utf-8 -*-

# generate a list of square [1, 11)
l1 = [x * x for x in range(1, 11)]
print(l1)

# even numbers
l2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l2)

# 全排列
l3 = [n + m for n in 'ABC' for m in 'XYZ']
print(l3)

# Convert to upper case
lowers = ['apple', 'orange', 'banana']
uppers = [s.upper() for s in lowers]
print(uppers)


