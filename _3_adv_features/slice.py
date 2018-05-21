# -*- coding: utf-8 -*-
# Every time function slice return a new object

students = ['Tom', 'Mary', 'Ken', 'Billy', 'Mike']

# Get continuously subset of a range

slice1 = students[0:3]
print(slice1)

slice2 = students[:3]
print(slice2)

slice3 = students[-3:]  # last three
print(slice3)

slice4 = students[2:4]  # 3rd & 4th
print(slice4)

slice5 = students[:]  # copy
print(slice5)

# Discontinuous subset skipped by a step
print(list(range(100)[0:20:2]))
print(list(range(100)[::5]))

# string can be sliced
print('abcde'[0:3])

