""" Sample to find common keys between 2 dictionaries """

d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

d2 = {
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

print(d1.keys() & d2.keys())  # intersection
print(d1.keys() | d2.keys())  # union
print(d1.keys() - d2.keys())  # diff
