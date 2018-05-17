# -*- coding: utf-8 -*-

# simple for-loop
animals = [1, 2, 3, 4, 5]
for o in animals:
    print(o)

# for-loop using range [0,100)
sum = 0
for i in range(0, 100):  # also can be `range(100)` in short
    sum = sum + i
print(sum)

# while-loop
sum = 0
i = 0
while i < 100:
    sum = sum + i
    i = i + 1
print(sum)

# while-loop with break
sum = 0
i = 0
while i < 100:
    if i >= 50:
        break
    sum = sum + i
    i = i + 1
print(sum)
