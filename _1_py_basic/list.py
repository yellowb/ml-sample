# -*- coding: utf-8 -*-
# Samples for List
animals = ['dog', 'cat', 'pig']
print(animals)
print(animals[2])
print(animals[-1])  # access by reversed index

# append element
animals.append('cow')
print(animals)

# insert element into specified position
animals.insert(1, 'duck')
print(animals)

# remove element
animals.pop()  # remove the tail
print(animals)
animals.pop(1)  # remove by specified position
print(animals)

# modify by index
animals[1] = 'chick'
print(animals)

# 2-d array
animals.append([1, 2, 3])
print(animals)
print(animals[3][1])
