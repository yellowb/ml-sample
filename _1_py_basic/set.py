# -*- coding: utf-8 -*-

# simple set, constructed by a list, will auto remove duplicated values
s = {1, 1, 2, 3}
print(s)

# duplicated values will not be added
s.add(1)
s.add(4)
print(s)

# remove key
s.remove(4)
print(s)

# set operation
s2 = {2, 3, 4}
print(s2.intersection(s))
print(s2 & s)  # shortcut
print(s2.difference(s))
print(s2 - s)  # shortcut
print(s2.union(s))
print(s2 | s)  # shortcut


